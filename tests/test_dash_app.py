import sys
import os

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from task_3_dash_app import app


def test_header_present():
    header = app.layout.children[0]
    assert header.children == "Pink Morsel Sales Analysis"


def test_region_picker_present():
    radio = app.layout.children[2]
    assert radio.id == "region-filter"


def test_graph_present():
    graph = app.layout.children[3]
    assert graph.id == "sales-line-chart"