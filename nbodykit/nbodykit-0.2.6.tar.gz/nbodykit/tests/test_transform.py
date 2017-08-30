from runtests.mpi import MPITest
from nbodykit.lab import *
from nbodykit import setup_logging
from nbodykit.transform import ConstantArray
import pytest

# debug logging
setup_logging("debug")

@MPITest([1, 4])
def test_sky_to_cartesian(comm):

    cosmo = cosmology.Planck15
    CurrentMPIComm.set(comm)

    # make source
    s = RandomCatalog(csize=100, seed=42)

    # ra, dec, z
    s['z']   = s.rng.normal(loc=0.5, scale=0.1, size=s.size)
    s['ra']  = s.rng.uniform(low=110, high=260, size=s.size)
    s['dec'] = s.rng.uniform(low=-3.6, high=60., size=s.size)

    # make the position array
    s['Position1'] = transform.SkyToCartesion(s['ra'], s['dec'], s['z'], cosmo)

    # requires dask array
    with pytest.raises(TypeError):
        s['Position1'] = transform.SkyToCartesion(s['ra'].compute(), s['dec'], s['z'], cosmo)

@MPITest([1, 4])
def test_stack_columns(comm):
    CurrentMPIComm.set(comm)

    # make source
    s = RandomCatalog(csize=100, seed=42)

    # add x,y,z
    s['x'] = s.rng.uniform(0, 2600., size=s.size)
    s['y'] = s.rng.uniform(0, 2600., size=s.size)
    s['z'] = s.rng.uniform(0, 2600., size=s.size)

    # stack
    s['Position'] = transform.StackColumns(s['x'], s['y'], s['z'])

    # test equality
    x, y, z = s.compute(s['x'], s['y'], s['z'])
    pos = numpy.vstack([x,y,z]).T
    numpy.testing.assert_array_equal(pos, s['Position'])

    # requires dask array
    with pytest.raises(TypeError):
        s['Position'] = transform.StackColumns(x,y,z)

@MPITest([1, 4])
def test_combine(comm):
    CurrentMPIComm.set(comm)

    # make two sources
    s1 = UniformCatalog(3e-6, 2600)
    s2 = UniformCatalog(3e-6, 2600)

    # concatenate all columns
    cat = transform.ConcatenateSources(s1, s2)

    # check the size and columns
    assert cat.size == s1.size + s2.size
    assert set(cat.columns) == set(s1.columns)

    # only one column
    cat = transform.ConcatenateSources(s1, s2, columns='Position')
    pos = numpy.concatenate([s1['Position'], s2['Position']], axis=0)
    numpy.testing.assert_array_equal(pos, cat['Position'])

    # fail on invalid column
    with pytest.raises(ValueError):
        cat = transform.ConcatenateSources(s1, s2, columns='InvalidColumn')

@MPITest([1])
def test_constarray(comm):
    a = ConstantArray(1.0, 1, chunks=1000)
    assert len(a) == 1
    print(a.shape)
    assert a.shape == (1,)
    a = ConstantArray([1.0, 1.0], 1, chunks=1000)
    assert a.shape == (1, 2)

    a = ConstantArray([1.0, 1.0], 3, chunks=1000)
    assert a.shape == (3, 2)
