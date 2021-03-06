# -*- coding: utf-8 -*-
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

response.logo = A(B("StopStalk"), _class="navbar-brand",
                  _href=URL('default', 'index'),
                  _id="web2py-logo")
response.title = request.application.replace('_',' ').title()
response.subtitle = ''

response.meta.author = 'StopStalk admin@stopstalk.com'
response.meta.description = 'Retrieves submissions of friends\' from various competitive websites and analyse them'
response.meta.keywords = 'stopstalk, raj454raj, competitive programming, algorithms, algorithmic progress'
response.meta.generator = ''

response.google_analytics_id = None

response.menu = []

def get_tooltip_data(tooltip):
    return dict(position="bottom", delay="40", tooltip=tooltip)

if session.user_id:
    response.menu += [
        (I(_class="fa fa-inbox fa-2x tooltipped",
           data=get_tooltip_data("Notifications")),
         False,
         URL('default', 'notifications'), []),
        (I(_class="fa fa-users fa-2x tooltipped",
           data=get_tooltip_data("Friend requests")),
         False,
         URL('user', 'friend_requests'), []),
        (I(_class="fa fa-search fa-2x tooltipped",
           data=get_tooltip_data("Search friends")),
         False,
         URL('default', 'search'), []),
        (I(_class="fa fa-plus-circle fa-2x tooltipped",
           data=get_tooltip_data("Add Custom Friend")),
         False,
         URL('user', 'custom_friend'), []),
        (I(_class="fa fa-pencil fa-2x tooltipped",
           data=get_tooltip_data("Edit Custom Friend Details")),
         False,
         URL('user', 'edit_custom_friend_details'), []),
    ]

response.menu += [(I(_class="fa fa-calendar-check-o fa-2x tooltipped",
                     data=get_tooltip_data("Upcoming Contests")),
                   False,
                   URL('default', 'contests'), []),
                  (I(_class="fa fa-bar-chart fa-2x tooltipped",
                     data=get_tooltip_data("Leaderboard")),
                   False,
                   URL('default', 'leaderboard'), []),
                  (I(_class="fa fa-line-chart fa-2x tooltipped",
                     data=get_tooltip_data("Trending problems")),
                   False,
                   URL('problems', 'trending'), []),
                  (I(_class="fa fa-filter fa-2x tooltipped",
                     data=get_tooltip_data("Submission Filters")),
                   False,
                   URL('default', 'filters'), []),
                  (I(_class="fa fa-tag fa-2x tooltipped",
                     data=get_tooltip_data("Search by tags")),
                   False,
                   URL('problems', 'tag'), []),
                  (I(_class="fa fa-question fa-2x tooltipped",
                     data=get_tooltip_data("FAQs")),
                   False,
                   URL('default', 'faq'), []),
                  (I(_class="fa fa-phone fa-2x tooltipped",
                     data=get_tooltip_data("Contact Us")),
                  False,
                  URL('default', 'contact_us'), [])]

if "auth" in locals(): auth.wikimenu()

# =============================================================================
