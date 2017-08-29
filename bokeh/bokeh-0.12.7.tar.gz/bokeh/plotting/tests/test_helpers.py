from mock import mock

import pytest

from bokeh.models import ColumnDataSource, CDSView, Marker
from bokeh.models.ranges import Range1d, DataRange1d, FactorRange
from bokeh.models.scales import LinearScale, LogScale, CategoricalScale
from bokeh.plotting import Figure
from bokeh.plotting.helpers import (_get_legend_item_label, _get_scale,
                                    _get_range, _stack, _glyph_function,
                                    _RENDERER_ARGS)


def test__stack_raises_when_spec_in_kwargs():
    with pytest.raises(ValueError) as e:
        _stack(['a', 'b'], 'foo', 'bar', foo=10)

    assert str(e).endswith("Stack property 'foo' cannot appear in keyword args")

    with pytest.raises(ValueError) as e:
        _stack(['a', 'b'], 'foo', 'bar', bar=10)

    assert str(e).endswith("Stack property 'bar' cannot appear in keyword args")

def test__stack_raises_when_kwargs_list_lengths_differ():
    with pytest.raises(ValueError) as e:
        _stack(['a', 'b'], 'foo', 'bar', baz=[1, 2], quux=[3,4,5])

    assert str(e).endswith("Keyword argument sequences for broadcasting must all be the same lengths. Got lengths: [2, 3]")

def test__stack_raises_when_kwargs_list_lengths_and_stackers_lengths_differ():
    with pytest.raises(ValueError) as e:
        _stack(['a', 'b', 'c'], 'foo', 'bar', baz=[1, 2], quux=[3,4])

    assert str(e).endswith("Keyword argument sequences for broadcasting must be the same length as stackers")

def test__stack_broadcast_with_no_kwargs():
    stackers = ['a', 'b', 'c', 'd']
    kws = _stack(stackers, 'start', 'end')
    assert len(kws) == len(stackers)
    for i, kw in enumerate(kws):
        assert set(['start', 'end']) == set(kw.keys())
        assert list(kw['start']['expr'].fields) == stackers[:i]
        assert list(kw['end']['expr'].fields) == stackers[:(i+1)]

def test__stack_broadcast_with_scalar_kwargs():
    stackers = ['a', 'b', 'c', 'd']
    kws = _stack(stackers, 'start', 'end', foo=10, bar="baz")
    assert len(kws) == len(stackers)
    for i, kw in enumerate(kws):
        assert set(['start', 'end', 'foo', 'bar']) == set(kw.keys())
        assert list(kw['start']['expr'].fields) == stackers[:i]
        assert list(kw['end']['expr'].fields) == stackers[:(i+1)]
        assert kw['foo'] == 10
        assert kw['bar'] == "baz"

def test__stack_broadcast_with_list_kwargs():
    stackers = ['a', 'b', 'c', 'd']
    kws = _stack(stackers, 'start', 'end', foo=[10, 20, 30, 40], bar="baz")
    assert len(kws) == len(stackers)
    for i, kw in enumerate(kws):
        assert set(['start', 'end', 'foo', 'bar']) == set(kw.keys())
        assert list(kw['start']['expr'].fields) == stackers[:i]
        assert list(kw['end']['expr'].fields) == stackers[:(i+1)]
        assert kw['foo'] == [10, 20, 30, 40][i]
        assert kw['bar'] == "baz"

# _get_legend_item_label
def test_if_legend_is_something_exotic_that_it_is_passed_directly_to_label():
    kwargs = {
        'legend': {'field': 'milk'}
    }
    label = _get_legend_item_label(kwargs)
    assert label == {'field': 'milk'}


def test_if_legend_is_a_string_but_no_source_then_label_is_set_as_value():
    kwargs = {
        'legend': 'label'
    }
    label = _get_legend_item_label(kwargs)
    assert label == {'value': 'label'}


def test_if_legend_is_a_string_and_source_with_that_column_then_field():
    kwargs = {
        'legend': 'label',
        'source': ColumnDataSource(dict(label=[1, 2]))
    }
    label = _get_legend_item_label(kwargs)
    assert label == {'field': 'label'}


def test_if_legend_is_a_string_and_source_without_column_name_then_value():
    kwargs = {
        'legend': 'not_a_column_label',
        'source': ColumnDataSource(dict(label=[1, 2]))
    }
    label = _get_legend_item_label(kwargs)
    assert label == {'value': 'not_a_column_label'}

def test__get_scale_numeric_range_linear_axis():
    s = _get_scale(Range1d(), "linear")
    assert isinstance(s, LinearScale)

    s = _get_scale(Range1d(), "datetime")
    assert isinstance(s, LinearScale)

    s = _get_scale(Range1d(), "auto")
    assert isinstance(s, LinearScale)

def test__get_scale_numeric_range_log_axis():
    s = _get_scale(DataRange1d(), "log")
    assert isinstance(s, LogScale)

def test__get_scale_factor_range():
    s = _get_scale(FactorRange(), "auto")
    assert isinstance(s, CategoricalScale)

def test__get_range_with_None():
    r = _get_range(None)
    assert isinstance(r, DataRange1d)

def test__get_range_with_Range():
    for t in [Range1d, DataRange1d, FactorRange]:
        rng = t()
        r = _get_range(rng)
        assert r is rng

def test__get_range_with_string_seq():
    f = ["foo" ,"end", "baz"]
    for t in [list, tuple]:
        r = _get_range(t(f))
        assert isinstance(r, FactorRange)
        # FactorRange accepts Seq, but _get_range always sets a list copy
        assert r.factors == f

def test__get_range_with_float_bounds():
    r = _get_range((1.2, 10))
    assert isinstance(r, Range1d)
    assert r.start == 1.2
    assert r.end == 10

    r = _get_range([1.2, 10])
    assert isinstance(r, Range1d)
    assert r.start == 1.2
    assert r.end == 10

def test_get_range_with_pandas_group():
    from bokeh.sampledata.iris import flowers
    g = flowers.groupby('species')
    r = _get_range(g)
    assert isinstance(r, FactorRange)
    assert r.factors == ['setosa', 'versicolor', 'virginica'] # should always be sorted

# TODO: ideally, the list of arguments should be received directly from
# GlyphRenderer, but such case requires a system that would be able to generate
# acceptable values for parameters
_renderer_args_values = {
    'name': [None, '', 'test name'],
    'x_range_name': [None, '', 'x range'],
    'y_range_name': [None, '', 'y range'],
    'level': [None, 'overlay'],
    'view': [None, CDSView(source=None)],
    'visible': [None, False, True],
    'muted': [None, False, True]
}
@pytest.mark.parametrize('arg,values', [(arg, _renderer_args_values[arg])
                                        for arg in _RENDERER_ARGS])
def test__glyph_receives_renderer_arg(arg, values):
    for value in values:
        with mock.patch('bokeh.plotting.helpers.GlyphRenderer', autospec=True) as gr_mock:
            fn = _glyph_function(Marker)
            fn(Figure(), x=0, y=0, **{arg: value})
            _, kwargs = gr_mock.call_args
            assert arg in kwargs and kwargs[arg] == value
