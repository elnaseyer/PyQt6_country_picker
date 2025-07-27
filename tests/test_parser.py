from country_picker.mainwindow import parse_country_data

def test_parse_country_data_returns_sorted_names():
    input_data = [
        {'name': "Sweden"},
        {'name': "Denmark"},
        {'name': "Norway"}
    ]

    expected = ["Denmark", "Norway", "Sweden"]
    result = parse_country_data(input_data)

    assert result == expected