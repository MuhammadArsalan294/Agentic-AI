Basic Syntax

The Markdown elements outlined in the original design document. # yani markdown text ky design ky liye use hoti hai



########################## Headings ############################

Headings

To create a heading, add number signs (#) in front of a word or phrase. The number of number signs you use should correspond to the heading level. For example, to create a heading level three (<h3>), use three number signs (e.g., ### My Header).

# Heading level 1           yaha underscore line bhi aye gi	    

## Heading level 2	        yaha underscore line bhi aye gi	 

### Heading level 3	        yaha underscore line nhi aye gi 

#### Heading level 4        yaha underscore line nhi aye gi

##### Heading level 5	    yaha underscore line nhi aye gi

###### Heading level 6 	    yaha underscore line nhi aye gi

####### After level 6 normal text

(Yani Heading ky liye hash # ky bad space dy kar heading likhein gay or space lzmi dein gay without space normal text show hoga.or agar first line or last line ky center main heading dalni hai tw bhi space dein gay space ky bghr normal text show hoga.
Ctrl Shift v (es sy preview README.md open hoga yaha sy heading check kar skty ky kasi a rhi))





"""""Alternate Syntax"""""

Alternatively, on the line below the text, add any number of == characters for heading level 1 or -- characters for heading level 2.

Heading level 1   
===============

OR
=

(Yani = aik bhi ho ya zyada bhi tw bari Heading ban jaye gi or underscore line bhi a jaye gi. or ye sath mila kr likhna agar space dy dia tw normal text ban jaye ga)

Heading level 2   
---------------

(Yani - aik bhi ho ya zyada bhi tw choti Heading ban jaye gi or underscore line bhi a jaye gi. or ye sath mila kr likhna agar spece dy dia tw normal text ban jaye ga)





Heading Best Practices:

# Here's a Heading


Try to put a blank line before...

# Heading

...and after a heading.


########################## Paragraphs ############################

Paragraphs

To create paragraphs, use a blank line to separate one or more lines of text.


I really like using Markdown.

I think I'll use it to format all of my documents from now on.

(Agr koi cheez continue hai wo paragraph hai jaha line change ki paragraph khtm
means ky aik paragraph ky bad dusra start karne ky liye enter press karna hai or center main line chorni hai tw next paragraph ban jaye ga agar enter press kar ky center main line nhi chorein gay tw aik he paragraph chlta rhy ga.)

Paragraph Best Practices:

Don't put tabs or spaces in front of your paragraphs.

Keep lines left-aligned like this



########################## Line Breaks ############################

Line Breaks

To create a line break or new line (<br>), end a line with two or more spaces, and then type return.

This is the first line.  
And this is the second line.

(Jaha bhi line change krni ho waha 2 bar ya os sy zyada bar space dein or phir enter press kr dein aik bar space nhi dena)
(Ya phir <> bracket main br likh dein )

Line Break Best Practices:

First line with two spaces after.  
And the next line.

First line with the HTML tag after.<br>
And the next line.


########################## Emphasis(Bold or Italic) ############################

Emphasis

You can add emphasis by making text bold or italic.

"""""Bold"""""

To bold text, add two asterisks or underscores before and after a word or phrase. To bold the middle of a word for emphasis, add two asterisks without spaces around the letters.

I just love **bold text**.

I just love __bold text__.

Love**is**bold  best practice


Bold Best Practices:

Love**is**bold


"""""Italic"""""

To italicize text, add one asterisk or underscore before and after a word or phrase. To italicize the middle of a word for emphasis, add one asterisk without spaces around the letters.

Italicized text is the *cat's meow*.

Italicized text is the _cat's meow_.

A*cat*meow 

Italic Best Practices:

A*cat*meow


"""""Bold and Italic"""""

To emphasize text with bold and italics at the same time, add three asterisks or underscores before and after a word or phrase. To bold and italicize the middle of a word for emphasis, add three asterisks without spaces around the letters.


This text is ***really important***. best practice

This text is ___really important___.

This text is __*really important*__.

This text is **_really important_**.

This is really***very***important text.


Bold and Italic Best Practices:

This is really***very***important text.


########################## Blockquotes ############################


Blockquotes

To create a blockquote, add a > in front of a paragraph.

> Dorothy followed her through many of the beautiful rooms in her castle.

> Dorothy followed her through many of the beautiful rooms in her castle.
> The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wood.

(Ye dono aik paragraph main ayein gay)

"""""Blockquotes with Multiple Paragraphs"""""

Blockquotes can contain multiple paragraphs. Add a > on the blank lines between the paragraphs.

> Dorothy followed her through many of the beautiful rooms in her castle.
>
> The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wood.

(Yaha center main line space aye ga)


"""""Nested Blockquotes"""""

Blockquotes can be nested. Add a >> in front of the paragraph you want to nest.

> Dorothy followed her through many of the beautiful rooms in her castle.
>
>> The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wood.
>>>The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wood.


"""""Blockquotes with Other Elements"""""

Blockquotes can contain other Markdown formatted elements. Not all elements can be used — you’ll need to experiment to see which ones work.

> #### The quarterly results look great!
>
> - Revenue was off the chart.
> - Profits were higher than ever.
>
>  *Everything* is going according to **plan**.



######################## List(Ordered and Unordered)  ###########################

Lists

You can organize items into ordered and unordered lists.

"""""Ordered Lists"""""

To create an ordered list, add line items with numbers followed by periods. The numbers don’t have to be in numerical order, but the list should start with the number one.

1. First item
2. Second item
3. Third item
4. Fourth item

1. First item
1. Second item
1. Third item
1. Fourth item

1. First item
8. Second item
3. Third item
5. Fourth item

1. First item
2. Second item
3. Third item
    1. Indented item
    1. Indented item
4. Fourth item

1. First item     
2. Second item

(Dot ky bad space lazmi do agar space nhi do gay tw ye dono aik line main ajayein gay)


Ordered List Best Practices:

1. First item
2. Second item


"""""Unordered Lists"""""

To create an unordered list, add dashes (-), asterisks (*), or plus signs (+) in front of line items. Indent one or more items to create a nested list.

- First item
- Second item
- Third item
- Fourth item

* First item
* Second item
* Third item
* Fourth item

+ First item
+ Second item
+ Third item
+ Fourth item

- First item
- Second item
- Third item
    - Indented item
    - Indented item
- Fourth item

Unordered List Best Practices:

- First item
- Second item
- Third item
- Fourth item

(yaha bhi -,+,* ho es ky bad space dena lazmi hai space nhi dein gay tw ye mil kar a jaye ga)


"""""Starting Unordered List Items With Numbers"""""

If you need to start an unordered list item with a number followed by a period, you can use a backslash (\) to escape the period.

- 1968\. A great year!
- I think 1969 was second best.


"""""Adding Elements in Lists"""""

To add another element in a list while preserving the continuity of the list, indent the element four spaces or one tab, as shown in the following examples.

"""""Paragraphs"""""

* This is the first list item.
* Here's the second list item.

    I need to add another paragraph below the second list item.

* And here's the third list item.


"""""Blockquotes"""""

* This is the first list item.
* Here's the second list item.

    > A blockquote would look great below the second list item.

* And here's the third list item.


"""""Code Blocks"""""

Code blocks are normally indented four spaces or one tab. When they’re in a list, indent them eight spaces or two tabs. 

1. Open the file.
2. Find the following code block on line 21:

        <html>
          <head>
            <title>Test</title>
          </head>

3. Update the title to match the name of your website.



"""""Images"""""

1. Open the file containing the Linux mascot.
2. Marvel at its beauty.

    ![Tux, the Linux mascot](/assets/images/tux.png)
    
    ![image show nhi hui tw ye name show hoga](yaha image jis jga sy li os ka link aye ga)

3. Close the file.


"""""Lists"""""

You can nest an unordered list in an ordered list, or vice versa.

1. First item
2. Second item
3. Third item
    - Indented item
    - Indented item
4. Fourth item



######################## Code  ###########################

Code

To denote a word or phrase as code, enclose it in backticks (`).

At the command prompt, type `nano`.


######################## Escaping Backticks  ###########################

Escaping Backticks

If the word or phrase you want to denote as code includes one or more backticks, you can escape it by enclosing the word or phrase in double backticks (``).
    

``Use `code` in your Markdown file.``

######################## Code Blocks ###########################

Code Blocks

To create code blocks, indent every line of the block by at least four spaces or one tab.

    <html>
      <head>
      </head>
    </html>

(Lazmi hai ky 4 spaces ya aik tab use karo code ko block main likhne ky liye agar kam use krein gay tw show nhi hoga code block)

######################## Horizontal Line  ###########################

Horizontal Rules

To create a horizontal rule, use three or more asterisks (***), dashes (---), or underscores (___) on a line by themselves.

***

---

______ ___________

(Lazmi hai ky 3 ya os sy zyada use karo agar kam use karo gay tw ye order ya unorder list main show hoga horizontal line nhi aye gi phir or spaces dy skey hain koi masla nhi hoga )


Horizontal Rule Best Practices:


Try to put a blank line before...

---

...and after a horizontal rule.



######################## Links  ###########################

Links

To create a link, enclose the link text in brackets (e.g., [Duck Duck Go]) and then follow it immediately with the URL in parentheses (e.g., (https://duckduckgo.com)).

My favorite search engine is [Duck Duck Go](https://duckduckgo.com).

[yaha link show hoga jasey Duck Duck Go](yaha jis link py jana hai wo aye ga jasey https://duckduckgo.com)


"""""Adding Titles"""""

You can optionally add a title for a link. This will appear as a tooltip when the user hovers over the link. To add a title, enclose it in quotation marks after the URL.

My favorite search engine is [Duck Duck Go](https://duckduckgo.com "The best search engine for privacy").

[Duck Duck Go link py jab hower krein gay tw ye show hoga jasey "The best search engine for privacy"]


"""""URLs and Email Addresses"""""

To quickly turn a URL or email address into a link, enclose it in angle brackets.

<https://www.markdownguide.org>

<fake@example.com>

(ye url ya link bnany ky liye jasey email tw <> bracket ka use karna hai or bracket or jo bech main link dia hai es main space nhi dena space ky sath <> bracket bhi show hon gay )


"""""Formatting Links""""" Yani link ka style change kr skty hai

To emphasize links, add asterisks before and after the brackets and parentheses. To denote links as code, add backticks in the brackets.

I love supporting the **[EFF](https://eff.org)**.  
This is the *[Markdown Guide](https://www.markdownguide.org)*.  
See the section on [`code`](#code).



"""""Reference-style Links"""""

Reference-style links are a special kind of link that make URLs easier to display and read in Markdown. Reference-style links are constructed in two parts: the part you keep inline with your text and the part you store somewhere else in the file to keep the text easy to read.

"""""Formatting the First Part of the Link"""""

The first part of a reference-style link is formatted with two sets of brackets. The first set of brackets surrounds the text that should appear linked. The second set of brackets displays a label used to point to the link you’re storing elsewhere in your document.

Although not required, you can include a space between the first and second set of brackets. The label in the second set of brackets is not case sensitive and can include letters, numbers, spaces, or punctuation.

This means the following example formats are roughly equivalent for the first part of the link:

[hobbit-hole][1]

[hobbit-hole] [1]



"""""Formatting the Second Part of the Link"""""

The second part of a reference-style link is formatted with the following attributes:

1. The label, in brackets, followed immediately by a colon and at least one space (e.g., [label]: ).
2. The URL for the link, which you can optionally enclose in angle brackets.
3. The optional title for the link, which you can enclose in double quotes, single quotes, or parentheses.


This means the following example formats are all roughly equivalent for the second part of the link:

[1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle

[1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle "Hobbit lifestyles"

[1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle 'Hobbit lifestyles'

[1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle (Hobbit lifestyles)

[1]: <https://en.wikipedia.org/wiki/Hobbit#Lifestyle> "Hobbit lifestyles"

[1]: <https://en.wikipedia.org/wiki/Hobbit#Lifestyle> 'Hobbit lifestyles'

[1]: <https://en.wikipedia.org/wiki/Hobbit#Lifestyle> (Hobbit lifestyles)

(yani jis jga py jana ho os py click kro)

You can place this second part of the link anywhere in your Markdown document. Some people place them immediately after the paragraph in which they appear while other people place them at the end of the document (like endnotes or footnotes).



"""""An Example Putting the Parts Together"""""

Say you add a URL as a standard URL link to a paragraph and it looks like this in Markdown:

In a hole in the ground there lived a hobbit. Not a nasty, dirty, wet hole, filled with the ends
of worms and an oozy smell, nor yet a dry, bare, sandy hole with nothing in it to sit down on or to
eat: it was a [hobbit-hole](https://en.wikipedia.org/wiki/Hobbit#Lifestyle "Hobbit lifestyles"), and that means comfort.


Though it may point to interesting additional information, the URL as displayed really doesn’t add much to the existing raw text other than making it harder to read. To fix that, you could format the URL like this instead:

In a hole in the ground there lived a hobbit. Not a nasty, dirty, wet hole, filled with the ends
of worms and an oozy smell, nor yet a dry, bare, sandy hole with nothing in it to sit down on or to
eat: it was a [hobbit-hole][1], and that means comfort.

[1]: <https://en.wikipedia.org/wiki/Hobbit#Lifestyle> "Hobbit lifestyles"


In both instances above, the rendered output would be identical:

In a hole in the ground there lived a hobbit. Not a nasty, dirty, wet hole, filled with the ends of worms and an oozy smell, nor yet a dry, bare, sandy hole with nothing in it to sit down on or to eat: it was a hobbit-hole, and that means comfort.

and the HTML for the link would be:

<a href="https://en.wikipedia.org/wiki/Hobbit#Lifestyle" title="Hobbit lifestyles">hobbit-hole</a>


Link Best Practices:

Markdown applications don’t agree on how to handle spaces in the middle of a URL. For compatibility, try to URL encode any spaces with %20. Alternatively, if your Markdown application supports HTML, you could use the a HTML tag.

[link](https://www.example.com/my%20great%20page)

<a href="https://www.example.com/my great page">link</a>


Parentheses in the middle of a URL can also be problematic. For compatibility, try to URL encode the opening parenthesis (() with %28 and the closing parenthesis ()) with %29. Alternatively, if your Markdown application supports HTML, you could use the a HTML tag.


[a novel](https://en.wikipedia.org/wiki/The_Milagro_Beanfield_War_%28novel%29)

<a href="https://en.wikipedia.org/wiki/The_Milagro_Beanfield_War_(novel)">a novel</a>


######################## Images  ###########################

Images

To add an image, add an exclamation mark (!), followed by alt text in brackets, and the path or URL to the image asset in parentheses. You can optionally add a title in quotation marks after the path or URL.

![The San Juan Mountains are beautiful!](/assets/images/san-juan-mountains.jpg "San Juan Mountains")



"""""Linking Images"""""

To add a link to an image, enclose the Markdown for the image in brackets, and then add the link in parentheses.

[![An old rock in the desert](/assets/images/shiprock.jpg "Shiprock, New Mexico by Beau Rogers")](https://www.flickr.com/photos/beaurogers/31833779864/in/photolist-Qv3rFw-34mt9F-a9Cmfy-5Ha3Zi-9msKdv-o3hgjr-hWpUte-4WMsJ1-KUQ8N-deshUb-vssBD-6CQci6-8AFCiD-zsJWT-nNfsgB-dPDwZJ-bn9JGn-5HtSXY-6CUhAL-a4UTXB-ugPum-KUPSo-fBLNm-6CUmpy-4WMsc9-8a7D3T-83KJev-6CQ2bK-nNusHJ-a78rQH-nw3NvT-7aq2qf-8wwBso-3nNceh-ugSKP-4mh4kh-bbeeqH-a7biME-q3PtTf-brFpgb-cg38zw-bXMZc-nJPELD-f58Lmo-bXMYG-bz8AAi-bxNtNT-bXMYi-bXMY6-bXMYv)


######################## Escaping Characters  ###########################

"""Escaping Characters"""

To display a literal character that would otherwise be used to format text in a Markdown document, add a backslash (\) in front of the character.

\* Without the backslash, this would be a bullet in an unordered list.

(Yaha space dene ya naw dene sy frk nhi parta jb bhi escape character ka use karna ho os sy phle backslash \  lga dein gay )



"""""Characters You Can Escape"""""

You can use a backslash to escape the following characters.


Character	Name
\	        backslash
`	        backtick (see also escaping backticks in code)
*	        asterisk
_	        underscore
{ }	        curly braces
[ ]	        brackets
< >	        angle brackets
( )	        parentheses
#	        pound sign
+	        plus sign
-	        minus sign (hyphen)
.	        dot
!	        exclamation mark
|	        pipe (see also escaping pipe in tables)


######################## HTML  ###########################

"""""HTML"""""

Many Markdown applications allow you to use HTML tags in Markdown-formatted text. This is helpful if you prefer certain HTML tags to Markdown syntax. For example, some people find it easier to use HTML tags for images. Using HTML is also helpful when you need to change the attributes of an element, like specifying the color of text or changing the width of an image.

To use HTML, place the tags in the text of your Markdown-formatted file.

This **word** is bold. This <em>word</em> is italic.


HTML Best Practices

For security reasons, not all Markdown applications support HTML in Markdown documents. When in doubt, check your Markdown application’s documentation. Some applications support only a subset of HTML tags.

Use blank lines to separate block-level HTML elements like <div>, <table>, <pre>, and <p> from the surrounding content. Try not to indent the tags with tabs or spaces — that can interfere with the formatting.

You can’t use Markdown syntax inside block-level HTML tags. For example, <p>italic and **bold**</p> won’t work.
