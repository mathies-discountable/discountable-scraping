from CleanContent.Functions.ExtractTextFromHTML import extract_text_from_html
from CleanContent.Functions.FilterLines import filter_lines
from CleanContent.Functions.RemoveUnnecessaryHtmlElements import remove_unnecessary_html_elements

def clean_content(raw_text, should_filter_lines):

    if raw_text is None:
        return None
    content = remove_unnecessary_html_elements(raw_text)
    content = extract_text_from_html(content)
    content_length_before_filtering = len(content.split('\n'))

    if should_filter_lines:
        content = filter_lines(content) 
        content_length_after_filtering = len(content.split('\n'))

        #precentage_of_filtered_lines = (content_length_before_filtering - content_length_after_filtering) / content_length_before_filtering * 100
        #print("Anteil der gefilterten Zeilen: " + str(precentage_of_filtered_lines) + "%")

    content = content.replace('\n', ' ')

    return content