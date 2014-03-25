from __future__ import division, absolute_import, print_function

import numpy as np
from numpy.testing import TestCase, assert_

import numbers
from numpy.core.numerictypes import sctypes

class ABC(TestCase):
    def test_floats(self):
        for t in sctypes['float']:
            assert_(isinstance(t(), numbers.Real), 
                    "{} is not instance of Real".format(t.__name__))
            assert_(issubclass(t, numbers.Real),
                    "{} is not subclass of Real".format(t.__name__))
            assert_(not isinstance(t(), numbers.Rational), 
                    "{} is instance of Rational".format(t.__name__))
            assert_(not issubclass(t, numbers.Rational),
                    "{} is subclass of Rational".format(t.__name__))

    def test_complex(self):
        for t in sctypes['complex']:
            assert_(isinstance(t(), numbers.Complex), 
                    "{} is not instance of Complex".format(t.__name__))
            assert_(issubclass(t, numbers.Complex),
                    "{} is not subclass of Complex".format(t.__name__))
            assert_(not isinstance(t(), numbers.Real), 
                    "{} is instance of Real".format(t.__name__))
            assert_(not issubclass(t, numbers.Real),
                    "{} is subclass of Real".format(t.__name__))

    def test_int(self):
        for t in sctypes['int']:
            assert_(isinstance(t(), numbers.Integral), 
                    "{} is not instance of Integral".format(t.__name__))
            assert_(issubclass(t, numbers.Integral),
                    "{} is not subclass of Integral".format(t.__name__))

    def test_uint(self):
        for t in sctypes['uint']:
            assert_(isinstance(t(), numbers.Integral), 
                    "{} is not instance of Integral".format(t.__name__))
            assert_(issubclass(t, numbers.Integral),
                    "{} is not subclass of Integral".format(t.__name__))


