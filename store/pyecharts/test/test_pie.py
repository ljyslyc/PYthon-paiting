from unittest.mock import patch

from nose.tools import assert_equal

from example.commons import Faker
from pyecharts import options as opts
from pyecharts.charts import Pie


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_pie_base(fake_writer):
    c = (
        Pie()
        .add("", [list(z) for z in zip(Faker.choose(), Faker.values())])
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    c.render()
    _, content = fake_writer.call_args[0]
    assert_equal(c.theme, "white")
    assert_equal(c.renderer, "canvas")
