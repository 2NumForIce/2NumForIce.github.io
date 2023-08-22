# Very Cheap Page Generator (still working on web skills)
#
# Copyright (C) 2023 2NumForIce
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

# Make string
page = """
<!DOCTYPE html>
<html>
\t<head>
\t\t<title>
"""

# Function
def inp(x):
	global page
	page += input(x)

# Browser title
inp("Enter the browser display title: ")

page += """</title>
    \t\t<meta name="robots" content="noindex">
	\t\t<link rel="stylesheet" href="static/style.css">
    \t</head>
    \t<body>
"""
print(page)
# Title
inp("Enter the title: ")
