# Component plug-ins
See the illustration below of all the components in place, and the following
list for a description of each of the components. The image is [a Google Drawing](https://docs.google.com/drawings/d/1MRs86lJb0NS-8j6yqWynjOvJY7woKWEDBh7ebeluBmY).

![Components](https://docs.google.com/drawings/d/1MRs86lJb0NS-8j6yqWynjOvJY7woKWEDBh7ebeluBmY/export/png)

## Standard components (Text, Image, Columns et c)
These components are standard (or third-party) Django CMS plug-ins.

* Text is a WYSIWYG text area
* Image is a simple image with optional caption
* Columns let editor define two or more same-width columns for arbitrary content

## Custom plug-ins
These plug-ins are custom built for zetkin.org. In alphabetical order:

### Article (container)
* Container for elements that are part of an article
* Can contain Section Heads, Text, Image and more

### Blurb
* Can be used standalone, in columns, or in a Blurb Grid
* Can have an icon, a dotted line, or nothing
* Can have one or two buttons or links

### Blurb Grid
* Contains blurbs and aligns them in a grid

### FAQ Accordion
* Contains a defined set of frequently asked questions
* Accordion where user can open/close answers

### Feature
* Contains an image and content next to it
* Content can be anything, e.g. blurbs

### Feature Grid
* Contains Features and alternates them left/right

### History Timeline
* Contains a defined set of historic events
* Each event has a header and a short text
* Alternates events left/right

### Media Hero
* Underlined header and text
* Screenshot or video
* Call to action button

### Quote Hero
* Photo
* Underlined quote text and citation text
* Call to action link

### Section Head
* Contains a headline, dotted lines and text
* Headline and dotted lines are optional

### Simple Hero
* Can be centered, left or right aligned
* Contains text
* Call to action link
