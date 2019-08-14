#!/usr/bin/env python

#####################################################################
# Software License Agreement (BSD License)
#
# Copyright (c) 2019, Rigel Madraswalla.
# All rights reserved.
#####################################################################

import json
import some_complicated_machine_learning_algorithm as machine_learning

# Creates a news aricle and saves it to the specified file name.
def make_articles(configs):

    # Perform the article creation for every set of parameters specifed. This is
    #  typically the bread and butter of any automation script: the ability to
    #  perform the task on a LARGE set of data.
    for config in configs:

        # Create a blank article, an item that we can put our text onto,
        #  eg. the final news article
        article_file = open_file(config["file_name"])

        # Attach the thumbnail image at the specified url
        attach_thumbnail_image(config["thumbnail_picture"], article_file)

        # Handle the headline, evaulate and write the headline to the article
        #  document
        handle_headline(config["title"], article_file)

        # Handle the subtitle
        handle_subtitle(config["subtitle"], article_file)

        # Create 1 paragraph outlining what the new information is,
        #  and what source it came from.
        handle_source(config["source"], article_file)

        # Create paragraphs (up to 3) detailing previous knowledge about the product
        #  based on other articles
        handle_previous_knowledgebase(config["previous_knowledgebase"], \
            article_file)

        # Create 1 paragraph outlining when we can expect future information to be
        #  released/uncovered regarding this product
        handle_future_expected_information(config["future_expected_information"], \
            article_file)

################## HELPER FUNCTIONS ###################

# Evaluates the headline size and writes the headline to the article
def handle_headline(headline, article_file):
    # Check the size of the headline
    if (headline.number_of_words() <= 14):
        # Write the headline of the article
        article_file.write_in_english(
            content = headline,
            type = "headline"
        )
    else:
        # Raise an error if the headline is too long
        raise ("Article headline is above average length, \
                reduce words or headline will not fit \
                on a website thumbnail!")

# Evaluates the subtitle size and writes the subtitle to the article
def handle_subtitle(subtitle, article_file):
    # Check the size of the subtitle
    if (subtitle.number_of_sentences() == 1):
        # Write the subtitle of the article
        article_file.write_in_english(
            content = subtitle,
            type = "subtitle"
        )
    else:
        # Raise an error if the title is too long
        raise ("Article must have a subtitle of EXACTLY 1 sentence.")

# Accesses the URL of the source and uses machine learning to develop a
#  source paragraph
def handle_source(source, article_file):

    # If the source is of type other, use the manual description
    if (source["type"] == "other"):
        description = source["manual_description"]

    # Else, use machine learning to generate a description from url
    else:
        description = machine_learning.generate_description_from_url(
            type = source["type"],
            url = source["url"]
        )

    # Write the description, manual or machine learning, to the article
    article_file.write_in_english(
        content = description,
        type = "paragraph"
    )

# Create up to 3 paragraphs amalgamating all previous sources included
def handle_previous_knowledgebase(previous_knowledgebase, article_file):

    # Go through each one of the specified sources and generate a description
    #  of what that source tells us about our current topic
    for each_entry in previous_knowledgebase:
        description.append(
            machine_learning.generate_description_from_url(
                url = each_entry["url"],
                addtional_info = each_entry["manual_analysis"]))

    # Trim the description to max 3 paragraphs to ensure short article length
    description.trim_the_fat(max_paragraphs = 3)

    # Write the description to the article
    article_file.write_in_english(
        content = description,
        type = "paragraph"
    )

# Create 1 paragraph detailing when we can expect more information on this topic
def handle_future_expected_information(future_expected_information, \
                                        article_file):

    # If the type of info is unsupported, use the provided manual_description
    if (future_expected_information["type"] == "other"):
        description = future_expected_information["manual_description"]

    # Else, use machine_learning to generate a blurb based on key info
    else:
        description = machine_learning.generate_future_info_blurb(
            type = future_expected_information["type"],
            name = future_expected_information["name"],
            date = future_expected_information["date"],
        )

    # Write the paragraph to the article
    article_file.write_in_english(
        content = description,
        type = paragraph
    )

# Retrieves the parameters specified in config.json
# @return The JSON of parameters
def get_config():
    with open("config.json", "r+") as config_file:
        return json.loads(config_file.read())

if __name__ == "__main__":
    config = get_config()
    make_articles(config)
