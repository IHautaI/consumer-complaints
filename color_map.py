import re
from bs4 import BeautifulSoup



def color_map(values):

    states = {
            'AK': 'Alaska',
            'AL': 'Alabama',
            'AR': 'Arkansas',
            'AS': 'American Samoa',
            'AZ': 'Arizona',
            'CA': 'California',
            'CO': 'Colorado',
            'CT': 'Connecticut',
            'DC': 'District of Columbia',
            'DE': 'Delaware',
            'FL': 'Florida',
            'GA': 'Georgia',
            'GU': 'Guam',
            'HI': 'Hawaii',
            'IA': 'Iowa',
            'ID': 'Idaho',
            'IL': 'Illinois',
            'IN': 'Indiana',
            'KS': 'Kansas',
            'KY': 'Kentucky',
            'LA': 'Louisiana',
            'MA': 'Massachusetts',
            'MD': 'Maryland',
            'ME': 'Maine',
            'MI': 'Michigan',
            'MN': 'Minnesota',
            'MO': 'Missouri',
            'MP': 'Northern Mariana Islands',
            'MS': 'Mississippi',
            'MT': 'Montana',
            'NA': 'National',
            'NC': 'North Carolina',
            'ND': 'North Dakota',
            'NE': 'Nebraska',
            'NH': 'New Hampshire',
            'NJ': 'New Jersey',
            'NM': 'New Mexico',
            'NV': 'Nevada',
            'NY': 'New York',
            'OH': 'Ohio',
            'OK': 'Oklahoma',
            'OR': 'Oregon',
            'PA': 'Pennsylvania',
            'PR': 'Puerto Rico',
            'RI': 'Rhode Island',
            'SC': 'South Carolina',
            'SD': 'South Dakota',
            'TN': 'Tennessee',
            'TX': 'Texas',
            'UT': 'Utah',
            'VA': 'Virginia',
            'VI': 'Virgin Islands',
            'VT': 'Vermont',
            'WA': 'Washington',
            'WI': 'Wisconsin',
            'WV': 'West Virginia',
            'WY': 'Wyoming'
            }

    states = states.keys() # because laziness

    #SVG map
    svg = open('USA.svg', 'r').read()
    soup = BeautifulSoup(svg)#, selfClosingTags=['defs', 'sodipodi:namedview'])

    #counties
    paths = soup.find_all('path')

    colors = ["#FFFFCC", "#FFEDA0", "#FED976", "#FEB24C", "#FD8D3C", "#FC4E2A", "#E31A1C", "#B10026"]


    # Change colors, replacing whole style instead of parsing for fill
    path_style = 'font-size:12px;fill-rule:nonzero;stroke:#000000;stroke-opacity:1;stroke-width:0.1;stroke-miterlimit:4;stroke-dasharray:none;stroke-linecap:butt;marker-start:none;stroke-linejoin:bevel;fill:'



    for p in paths:

        if p['id'] not in ["State_Lines", "separator"]:

            try:
                rate = values[p['inkscape:label'][-2:]]
            except:
                continue

            if rate > 7:
                color_class = 7
            elif rate > 6:
                color_class = 6
            elif rate > 5:
                color_class = 5
            elif rate > 4:
                color_class = 4
            elif rate > 3:
                color_class = 3
            elif rate > 2:
                color_class = 2
            elif rate > 1:
                color_class = 1
            else:
                color_class = 0


            color = colors[color_class]
            p['style'] = path_style + color

    return soup.prettify()
