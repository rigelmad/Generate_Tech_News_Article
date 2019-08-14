# README: Generate Tech News Article

## Purpose
This is a utility used to auto-generate a tech news article based on
specified parameters. The user should specify parameters in the `config.json` file, and then use the `generate_article.py` script to generate a coherent news article from the specified parameters.

## Documentation
### config.json
#### Configuration Paramters
**1. file_name**: The desired file name for this article

**2. thumbnail_picture**: The URL of the picture to appear on a website thumbnail.

**3. headline**: The headline of the article, keep between 5-12 words. Mention the name of a tech company or service for added attention.

**4. subtitle**: The subtitle, keep to one sentence. Reader should be able to understand the crux of the article by now.

**5. source**: The source of the information being addressed.
- In this release, the supported `type`s are:
```
"video",
"press_release",
"quote_from_source",
"tweet",
"other"
```
  - Sources with defined types (any type that is not `other`) will automatically be parsed and given a description using through a Machine Learning algorithm.
  - Sources of `"type" : "other"` must then be given a `manual_description` field to describe what the information is relaying.
- The `url` field indicates the source of the information, and will be [hyperlinked](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#links).

**6. previous_knowledgebase**: Articles that detail any previous information that is known about this product.
- The `url` tag is the location of the information, a Machine Learning algorithm will go through and draw analyses from each of the URLs specified, centering upon the topic of _this_ article.
- Any additional information can be specified in the `manual_analysis` portion, and will be fed into the creation of the description.
- A max of 3 paragraphs will be created to keep article length appropriate.

**7. future_expected_information**: When can we expect more information about this product, and through what medium?
- In this version, supported `type`s are:
```
"press_conference",
"product_release",
"convention",
"other"
```
  - Items with a `"type" : "other"` will require a `manual_description`.

#### Other Notes
- This version supports pseudo-markdown, meaning that in any manual description, a user may add two asterisks (\*\*) on either side of a statement to make that statement appear as a **BOLD SIDEBAR**, in proximity of that statement in the article. Sidebars will be rejected if they are greater than **10 words**.

### generate_article.py
#### Methodology
Run this script after specifying the parameters in `config.json` in order to create a news article. The script uses [INSERT COMPLICATED MACHINE LEARNING ALGORITHM NAME HERE] to parse information from sources, and uses natural language processing provided by the Google Home API to generate a coherent article.
