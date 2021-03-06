"""
    Copyright (c) 2015-2016 Raj Patel(raj454raj@gmail.com), StopStalk

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE.
"""

from .init import *

class Profile(object):
    """
        Class containing methods for retrieving
        submissions of user
    """

    # -------------------------------------------------------------------------
    def __init__(self, handle=""):
        """
            @param handle (String): Codeforces Handle
        """

        self.site = "CodeForces"
        self.handle = handle

    # -------------------------------------------------------------------------
    @staticmethod
    def get_tags(problem_link):
        """
            Get the tags of a particular problem from its URL

            @param problem_link (String): Problem URL
            @return (List): List of tags for that problem
        """

        response = get_request(problem_link)
        if response == -1 or response == {}:
            return ["-"]

        tags = BeautifulSoup(response.text, "lxml").find_all("span",
                                                             class_="tag-box")

        return map(lambda tag: tag.contents[0].strip(), tags)

    # -------------------------------------------------------------------------
    def get_submissions(self, last_retrieved):
        """
            Retrieve CodeForces submissions after last retrieved timestamp

            @param last_retrieved (DateTime): Last retrieved timestamp for the user
            @return (Dict): Dictionary of submissions containing all the
                            information about the submissions
        """

        if self.handle:
            handle = self.handle
        else:
            return -1

        url = "http://www.codeforces.com/api/user.status?handle=" + \
              handle + \
              "&from=1&count=50000"

        tmp = get_request(url, headers={"User-Agent": user_agent})

        if tmp == {} or tmp == -1:
            return tmp

        submissions = {handle: {1: {}}}
        all_submissions = tmp.json()
        if all_submissions["status"] != "OK":
            return submissions
        all_submissions = all_submissions["result"]
        it = 0
        for row in all_submissions:

            submissions[handle][1][it] = []
            submission = submissions[handle][1][it]
            append = submission.append

            curr = time.gmtime(row["creationTimeSeconds"] + 330 * 60)
            if curr <= last_retrieved:
                return submissions

            # Time of submission
            append(str(time.strftime("%Y-%m-%d %H:%M:%S", curr)))

            arg = "problem/"
            if len(str(row["contestId"])) > 3:
                arg = "gymProblem/"

            # Problem Name/URL
            problem_link = "http://www.codeforces.com/problemset/" + arg + \
                           str(row["contestId"]) + "/" + \
                           row["problem"]["index"]

            append(problem_link)
            problem_name = row["problem"]["name"]
            append(problem_name)

            # Problem status
            try:
                status = row["verdict"]
            except KeyError:
                status = "OTHER"
            submission_status = "AC"
            if status == "OK":
                submission_status = "AC"
            elif status == "WRONG_ANSWER":
                submission_status = "WA"
            elif status == "COMPILATION_ERROR":
                submission_status = "CE"
            elif status == "SKIPPED":
                submission_status = "SK"
            elif status == "RUNTIME_ERROR":
                submission_status = "RE"
            elif status == "TIME_LIMIT_EXCEEDED":
                submission_status = "TLE"
            elif status == "CHALLENGED":
                submission_status = "HCK"
            elif status == "MEMORY_LIMIT_EXCEEDED":
                submission_status = "MLE"
            # @ToDo: Is this a good and/or correct way?
            elif status == "TESTING":
                continue
            else:
                submission_status = "OTH"
            append(submission_status)

            # Points
            if submission_status == "AC":
                points = "100"
            elif submission_status == "HCK":
                points = "-50"
            else:
                points = "0"
            append(points)

            # Language
            append(row["programmingLanguage"])

            # View code link
            view_link = "http://www.codeforces.com/contest/" + \
                        str(row["contestId"]) + \
                        "/submission/" + \
                        str(row["id"])
            append(view_link)

            it += 1

        return submissions

# =============================================================================
