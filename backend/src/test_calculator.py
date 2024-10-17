import math
import re
import unittest
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_calc_add_negative_and_negative(self):
        self.assertEqual(self.calculator.addition(-3, -3), -6)

    def test_calc_add_natural_and_natural(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)

    def test_calc_add_int_and_str(self):
        error_message = "unsupported operand type(s) for +: 'int' and 'str'"
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.calculator.addition(1, "a")

    def test_calc_add_str_and_int(self):
        error_message = 'can only concatenate str (not "int") to str'
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.calculator.addition("a", 1)

    def test_calc_add_str_and_str(self):
        self.assertEqual(self.calculator.addition("a", "b"), "ab")

    def test_calc_add_notWhole_and_notWhole(self):
        self.assertEqual(self.calculator.addition(1.5, 1.5), 3.0)

    def test_calc_float_and_float(self):
        self.assertEqual(self.calculator.addition(1.9999999999999999, 0.0000000000000001), 2)

    def test_calc_add_inf_and_inf(self):
        self.assertEqual(self.calculator.addition(math.inf, math.inf), math.inf)

    def test_calc_add_int_and_negativeInf(self):
        result = self.calculator.addition(math.inf, -math.inf)
        self.assertTrue(math.isnan(result))

    def test_calc_add_negativeInf_and_negativeInf(self):
        self.assertEqual(self.calculator.addition(-math.inf, -math.inf), -math.inf)

    def test_calc_add_bool_and_bool(self):
        self.assertEqual(self.calculator.addition(True, True), 2)

    def test_calc_add_bool_and_bool_2(self):
        self.assertEqual(self.calculator.addition(True, False), 1)

    def test_calc_add_bool_and_bool_3(self):
        self.assertEqual(self.calculator.addition(False, False), 0)

    def test_calc_add_massive_and_massive(self):
        self.assertEqual(self.calculator.addition([1, 2, 3], ['a', 'b', 'c']), [1, 2, 3,'a', 'b', 'c'])

    def test_calc_add_list_and_int(self):
        error_message = 'can only concatenate list (not "int") to list'
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.calculator.addition([1, 2, 3], 2)

    def test_calc_add_list_and_str(self):
        error_message = 'can only concatenate list (not "str") to list'
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.calculator.addition([1, 2, 3], "a")

    def test_calc_add_tuple_and_tuple(self):
        self.assertEqual(self.calculator.addition(('red', 'blue', 'green'),('red', 'blue', 'green')),('red', 'blue', 'green', 'red', 'blue', 'green'))

    def test_calc_add_tuple_and_int(self):
        error_message = 'can only concatenate tuple (not "int") to tuple'
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.calculator.addition(('red', 'blue', 'green'), 1)

    def test_calc_add_tuple_and_str(self):
        error_message = 'can only concatenate tuple (not "str") to tuple'
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.calculator.addition(('red', 'blue', 'green'), "1")

    def test_calc_add_set_and_set(self):
        error_message = "unsupported operand type(s) for +: 'set' and 'set'"
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.calculator.addition({'black', 'blue', 'white'},{'black', 'blue', 'white'})

    def test_calc_add_dict_and_dict(self):
        error_message = "unsupported operand type(s) for +: 'dict' and 'dict'"
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.calculator.addition({'color': 'red', 'model': 'VC6', 'dimensions': '30x50'},{'color': 'red', 'model': 'VC6', 'dimensions': '30x50'})

    def test_calc_mult_negative_and_negative(self):
        self.assertEqual(self.calculator.multiplication(-1, -5), 5)

    def test_calc_mult_natural_and_natural(self):
        self.assertEqual(self.calculator.multiplication(1, 2), 2)

    def test_calc_mult_int_and_str(self):
        self.assertEqual(self.calculator.multiplication(3, "a"), "aaa")

    def test_calc_mult_str_and_int(self):
        self.assertEqual(self.calculator.multiplication("a", 3), "aaa")

    def test_calc_mult_str_and_str(self):
        error_message = "can't multiply sequence by non-int of type 'str'"
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.calculator.multiplication("a", "b")

    def test_calc_mult_notWhole_and_notWhole(self):
        self.assertEqual(self.calculator.multiplication(1.5, 1.5), 2.25)

    def test_calc_mult_float_and_float(self):
        self.assertEqual(self.calculator.multiplication(1.9999999999999999, 0.0000000000000001), 0.00000000000000019999999999999999)

    def test_calc_mult_int_and_int(self):
        self.assertEqual(self.calculator.multiplication(math.inf, 1), math.inf)

    def test_calc_mult_inf_and_zero(self):
        result = self.calculator.multiplication(math.inf, 0)
        self.assertTrue(math.isnan(result))

    def test_calc_mult_negativeInf_and_int(self):
        self.assertEqual(self.calculator.multiplication(-math.inf, 1000), -math.inf)

    def test_calc_mult_bool_and_bool_1(self):
        self.assertEqual(self.calculator.multiplication(True, True), 1)

    def test_calc_mult_bool_and_bool_2(self):
        self.assertEqual(self.calculator.multiplication(True, False), 0)

    def test_calc_mult_bool_and_bool_3(self):
        self.assertEqual(self.calculator.multiplication(False, False), 0)

    def test_calc_mult_list_and_int(self):
        self.assertEqual(self.calculator.multiplication([1, 2, 3], 4), [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3])

    def test_calc_mult_list_and_list(self):
        error_message = "can't multiply sequence by non-int of type 'list'"
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.calculator.multiplication([1, 2, 3], ['a', 'b', 'c'])

    def test_calc_mult_list_and_str(self):
        error_message = "can't multiply sequence by non-int of type 'str'"
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.calculator.multiplication([1, 2, 3], "a")

    def test_calc_mult_tuple_and_int(self):
        self.assertEqual(self.calculator.multiplication(('red', 'blue', 'green'), 4), ('red','blue', 'green', 'red','blue','green','red','blue','green','red','blue','green'))

    def test_calc_mult_tuple_and_tuple(self):
        error_message = "can't multiply sequence by non-int of type 'tuple'"
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.calculator.multiplication(('red', 'blue', 'green'), ('red', 'blue', 'green'))

    def test_calc_mult_tuple_and_str(self):
        error_message = "can't multiply sequence by non-int of type 'str'"
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.calculator.multiplication(('red', 'blue', 'green'), "1")

    def test_calc_mult_set_and_set(self):
        error_message = "unsupported operand type(s) for *: 'set' and 'set'"
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.calculator.multiplication({'black', 'blue', 'white'}, {'black', 'blue', 'white'})

    def test_mult_add_dict_and_dict(self):
        error_message = "unsupported operand type(s) for *: 'dict' and 'dict'"
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.calculator.multiplication({'color': 'red', 'model': 'VC6', 'dimensions': '30x50'},
                                     {'color': 'red', 'model': 'VC6', 'dimensions': '30x50'})

    def test_mult_add_dict_and_int(self):
        error_message = "unsupported operand type(s) for *: 'dict' and 'int'"
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.calculator.multiplication({'color': 'red', 'model': 'VC6', 'dimensions': '30x50'}, 2)

    def test_calc_sub_int_and_int(self):
        self.assertEqual(self.calculator.subtraction(1, 2), -1)

    def test_calc_sub_str_and_str(self):
        error_message = "unsupported operand type(s) for -: 'str' and 'str'"
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.calculator.subtraction("ab", "a")

    def test_calc_sub_str_and_int(self):
        error_message = "unsupported operand type(s) for -: 'str' and 'int'"
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.calculator.subtraction("a", 3)

    def test_calc_sub_str_and_float(self):
        error_message = "unsupported operand type(s) for -: 'str' and 'float'"
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.calculator.subtraction("a", 9.93)

    def test_calc_sub_notWhole_and_notWhole(self):
        self.assertEqual(self.calculator.subtraction(1.5, 1.5), 0)

    # приколы от путона
    def test_calc_sub_float_and_float(self):
        self.assertEqual(self.calculator.subtraction(1.9999999999999999, 0.0000000000000001), 2)

    def test_calc_sub_int_and_int_2(self):
        self.assertEqual(self.calculator.subtraction(math.inf, 1), math.inf)

    def test_calc_sub_int_and_int_3(self):
        result = self.calculator.subtraction(math.inf, math.inf)
        self.assertTrue(math.isnan(result))

    def test_calc_sub_negativeInf_and_int(self):
        self.assertEqual(self.calculator.subtraction(-math.inf, -1000), -math.inf)

    def test_calc_sub_bool_and_bool(self):
        self.assertEqual(self.calculator.subtraction(True, True), False)

    def test_calc_sub_bool_and_bool_2(self):
        self.assertEqual(self.calculator.subtraction(True, False), 1)

    def test_calc_sub_bool_and_bool_3(self):
        self.assertEqual(self.calculator.subtraction(False, False), 0)

    def test_calc_sub_list_and_int(self):
        error_message = "unsupported operand type(s) for -: 'list' and 'int'"
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.calculator.subtraction([1, 2, 3], 4)

    def test_calc_sub_list_and_list(self):
        error_message = "unsupported operand type(s) for -: 'list' and 'list'"
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.calculator.subtraction([1, 2, 3], ['a', 'b', 'c'])

    def test_calc_sub_list_and_str(self):
        error_message = "unsupported operand type(s) for -: 'list' and 'str'"
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.calculator.subtraction([1, 2, 3], "a")

    def test_calc_sub_tuple_and_int(self):
        error_message = "unsupported operand type(s) for -: 'tuple' and 'int'"
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.calculator.subtraction(('red', 'blue', 'green'), 4)

    def test_calc_sub_tuple_and_tuple(self):
        error_message = "unsupported operand type(s) for -: 'tuple' and 'tuple'"
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.calculator.subtraction(('red', 'blue', 'green'), ('red', 'blue', 'green'))

    def test_calc_sub_tuple_and_str(self):
        error_message = "unsupported operand type(s) for -: 'tuple' and 'str'"
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.calculator.subtraction(('red', 'blue', 'green'), "1")

    def test_calc_sub_set_and_set(self):
        self.assertEqual(self.calculator.subtraction({'black', 'blue', 'white'}, {'black', 'blue', 'white'}), set())

    def test_calc_sub_dict_and_dict(self):
        error_message = "unsupported operand type(s) for -: 'dict' and 'dict'"
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.calculator.subtraction({'color': 'red', 'model': 'VC6', 'dimensions': '30x50'},
                                     {'color': 'red', 'model': 'VC6', 'dimensions': '30x50'})

    def test_calc_sub_dict_and_int(self):
        error_message = "unsupported operand type(s) for -: 'dict' and 'int'"
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.calculator.subtraction({'color': 'red', 'model': 'VC6', 'dimensions': '30x50'}, 2)

    def test_calc_div_int_and_int(self):
        self.assertEqual(self.calculator.division(20, 4), 5)

    def test_calc_div_negative_and_negative(self):
        self.assertEqual(self.calculator.division(-6, -3), 2)

    def test_calc_div_int_and_int_2(self):
        self.assertEqual(self.calculator.division(1, 2), 0.5)

    def test_calc_div_str_and_str(self):
        error_message = "unsupported operand type(s) for /: 'str' and 'str'"
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.calculator.division("ab", "a")

    def test_calc_div_str_and_int(self):
        error_message = "unsupported operand type(s) for /: 'str' and 'int'"
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.calculator.division("a", 3)

    def test_calc_div_str_and_float(self):
        error_message = "unsupported operand type(s) for /: 'str' and 'float'"
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.calculator.division("a", 9.93)

    def test_calc_div_notWhole_and_notWhole(self):
        self.assertEqual(self.calculator.division(1.5, 1.5), 1)

    # приколы от путона
    def test_calc_div_float_and_float(self):
        self.assertEqual(self.calculator.division(1.9999999999999999, 0.0000000000000001), 2e+16)

    def test_calc_div_inf_and_int(self):
        self.assertEqual(self.calculator.division(math.inf, 1), math.inf)

    def test_calc_div_inf_and_inf(self):
        result = self.calculator.division(math.inf, math.inf)
        self.assertTrue(math.isnan(result))

    def test_calc_div_negativeInf_and_int(self):
        self.assertEqual(self.calculator.division(-math.inf, -1000), math.inf)

    def test_calc_div_bool_and_bool(self):
        self.assertEqual(self.calculator.division(True, True), True)

    def test_calc_div_bool_and_bool_2(self):
        self.assertEqual(self.calculator.division(True, False), None)

    def test_calc_div_bool_and_bool_3(self):
        self.assertEqual(self.calculator.division(False, False), None)

    def test_calc_div_list_and_int(self):
        error_message = "unsupported operand type(s) for /: 'list' and 'int'"
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.calculator.division([1, 2, 3], 4)

    def test_calc_div_list_and_list(self):
        error_message = "unsupported operand type(s) for /: 'list' and 'list'"
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.calculator.division([1, 2, 3], ['a', 'b', 'c'])

    def test_calc_div_list_and_str(self):
        error_message = "unsupported operand type(s) for /: 'list' and 'str'"
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.calculator.division([1, 2, 3], "a")

    def test_calc_div_tuple_and_int(self):
        error_message = "unsupported operand type(s) for /: 'tuple' and 'int'"
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.calculator.division(('red', 'blue', 'green'), 4)

    def test_calc_div_tuple_and_tuple(self):
        error_message = "unsupported operand type(s) for /: 'tuple' and 'tuple'"
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.calculator.division(('red', 'blue', 'green'), ('red', 'blue', 'green'))

    def test_calc_div_tuple_and_str(self):
        error_message = "unsupported operand type(s) for /: 'tuple' and 'str'"
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.calculator.division(('red', 'blue', 'green'), "1")

    def test_calc_div_set_and_set(self):
        error_message = "unsupported operand type(s) for /: 'set' and 'set'"
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.calculator.division({'black', 'blue', 'white'}, {'black', 'blue', 'white'})

    def test_sub_div_dict_and_dict(self):
        error_message = "unsupported operand type(s) for /: 'dict' and 'dict'"
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.calculator.division({'color': 'red', 'model': 'VC6', 'dimensions': '30x50'},
                                     {'color': 'red', 'model': 'VC6', 'dimensions': '30x50'})

    def test_sub_div_dict_and_int(self):
        error_message = "unsupported operand type(s) for /: 'dict' and 'int'"
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.calculator.division({'color': 'red', 'model': 'VC6', 'dimensions': '30x50'}, 2)

    def test_calc_abs_int(self):
        self.assertEqual(self.calculator.absolute(1), 1)

    def test_calc_abs_str(self):
        error_message = "bad operand type for abs(): 'str'"
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.calculator.absolute("ab")

    def test_calc_abs_set(self):
        error_message = "bad operand type for abs(): 'set'"
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.calculator.absolute({'as',1,1})

    def test_calc_abs_dict(self):
        error_message = "bad operand type for abs(): 'dict'"
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.calculator.absolute({'color': 111})

    def test_calc_abs_tuple(self):
        error_message = "bad operand type for abs(): 'tuple'"
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.calculator.absolute(('color', 'red', 'blue'))

    def test_calc_abs_inf(self):
        self.assertEqual(self.calculator.absolute(-math.inf), math.inf)

    def test_calc_abs_nan(self):
        result = self.calculator.absolute(math.nan)
        self.assertTrue(math.isnan(result))

    def test_calc_abs_inf_2(self):
        self.assertEqual(self.calculator.absolute(math.inf), math.inf)

    def test_calc_abs_int_2(self):
        self.assertEqual(self.calculator.absolute(-100000), 100000)

    def test_calc_ln_notWhole(self):
        self.assertEqual(self.calculator.ln(1.4), 0.3364722366212129)

    def test_calc_ln_int(self):
        self.assertEqual(self.calculator.ln(1), 0)

    def test_calc_ln_int_2(self):
        self.assertEqual(self.calculator.ln(2), 0.6931471805599453)

    def test_calc_ln_negative(self):
        error_message = "math domain error"
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(ValueError, escaped_error_message):
            self.calculator.ln(-1)

    def test_calc_ln_str(self):
        error_message = 'must be real number, not str'
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.calculator.ln("-1")

    def test_calc_ln_set(self):
        error_message = 'must be real number, not set'
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.calculator.ln({1,2,3})

    def test_calc_ln_tuple(self):
        error_message = 'must be real number, not tuple'
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.calculator.ln((1,2,3))

    def test_calc_ln_dict(self):
        error_message = 'must be real number, not dict'
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.calculator.ln({'blue': (1,2,3)})

    def test_calc_sqrt_notWhole(self):
        self.assertEqual(self.calculator.sqrt(1.6), 1.2649110640673518)

    def test_calc_sqrt_int(self):
        self.assertEqual(self.calculator.sqrt(1), 1)

    def test_calc_sqrt_int_2(self):
        self.assertEqual(self.calculator.sqrt(4), 2)

    def test_calc_sqrt_negative(self): # Это мнимая единица
        self.assertEqual(self.calculator.sqrt(-1), (6.123233995736766e-17+1j))

    def test_calc_sqrt_str(self):
        error_message = "unsupported operand type(s) for ** or pow(): 'str' and 'float'"
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.calculator.sqrt("-1")

    def test_calc_sqrt_set(self):
        error_message = "unsupported operand type(s) for ** or pow(): 'set' and 'float'"
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.calculator.sqrt({1, 2, 3})

    def test_calc_sqrt_tuple(self):
        error_message = "unsupported operand type(s) for ** or pow(): 'tuple' and 'float'"
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.calculator.sqrt((1, 2, 3))

    def test_calc_sqrt_dict(self):
        error_message = "unsupported operand type(s) for ** or pow(): 'dict' and 'float'"
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.calculator.sqrt({'blue': (1, 2, 3)})

    def test_calc_sqrt_int_3(self):
        self.assertEqual(self.calculator.sqrt(14), 3.7416573867739413)

    def test_calc_sqrt_negative_2(self):
        self.assertEqual(self.calculator.sqrt(-14), (2.2911043711093785e-16+3.7416573867739413j))

    def test_calc_log_int_and_int(self):
        self.assertEqual(self.calculator.log(1,5), 0)

    def test_calc_log_int_and_zero(self):
        error_message = 'math domain error'
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(ValueError, escaped_error_message):
            self.assertEqual(self.calculator.log(1, 0), 0)

    def test_calc_log_int_and_negative(self):
        error_message = 'math domain error'
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(ValueError, escaped_error_message):
            self.assertEqual(self.calculator.log(1, -1355.46), 0)

    def test_calc_log_int_and_str(self):
        error_message = 'must be real number, not str'
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.assertEqual(self.calculator.log(1, "1"), 0)

    def test_calc_log_int_and_set(self):
        error_message = 'must be real number, not set'
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.assertEqual(self.calculator.log(1, {"1"}), 0)

    def test_calc_log_int_and_tuple(self):
        error_message = 'must be real number, not tuple'
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.assertEqual(self.calculator.log(1, ("1", "1", 0)), 0)

    def test_calc_log_int_and_dict(self):
        error_message = 'must be real number, not dict'
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.assertEqual(self.calculator.log(1, {'color': "1",'blue': "1"}), 0)

    def test_calc_log_dict_and_int(self):
        error_message = 'must be real number, not dict'
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.assertEqual(self.calculator.log({'color': "1",'blue': "1"},1), 0)

    def test_calc_log_str_and_int(self):
        error_message = 'must be real number, not str'
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.assertEqual(self.calculator.log("1", 1), 0)

    def test_calc_log_set_and_int(self):
        error_message = 'must be real number, not set'
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.assertEqual(self.calculator.log({"1"},1), 0)

    def test_calc_log_tuple_and_int(self):
        error_message = 'must be real number, not tuple'
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.assertEqual(self.calculator.log(("1", "1", 0),1), 0)

    def test_calc_log_dict_and_int_2(self):
        error_message = 'must be real number, not dict'
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.assertEqual(self.calculator.log({'color': "1",'blue': "1"},1), 0)

    def test_calc_log_negative_and_int(self):
        error_message = 'math domain error'
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(ValueError, escaped_error_message):
            self.assertEqual(self.calculator.log(-10233,1),1)

    def test_calc_log_1_and_1(self):
        error_message = 'float division by zero'
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(ZeroDivisionError, escaped_error_message):
            self.assertEqual(self.calculator.log(1,1),1)

    def test_calc_log_int_and_int_1(self):
        self.assertEqual(self.calculator.log(123,213), 0.8975792041610647)

    def test_calc_root_int_and_int(self):
        self.assertEqual(self.calculator.nth_root(1, 5), 1)

    def test_calc_root_int_and_zero(self):
        error_message = 'float division by zero'
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(ZeroDivisionError, escaped_error_message):
            self.assertEqual(self.calculator.nth_root(1, 0), 0)

    def test_calc_root_int_and_negative(self):
        self.assertEqual(self.calculator.nth_root(1, -1355.46), 1)

    def test_calc_root_float_and_str(self):
        error_message = "unsupported operand type(s) for /: 'float' and 'str'"
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.assertEqual(self.calculator.nth_root(1, "1"), 0)

    def test_calc_root_float_and_set(self):
        error_message = "unsupported operand type(s) for /: 'float' and 'set'"
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.assertEqual(self.calculator.nth_root(1, {"1"}), 0)

    def test_calc_root_int_and_tuple(self):
        error_message = "must be real number, not tuple"
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.assertEqual(self.calculator.log(1, ("1", "1", 0)), 0)

    def test_calc_root_float_and_dict(self):
        error_message = "unsupported operand type(s) for /: 'float' and 'dict'"
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.assertEqual(self.calculator.nth_root(1, {'color': "1", 'blue': "1"}), 0)

    def test_calc_root_dict_and_float(self):
        error_message = "unsupported operand type(s) for ** or pow(): 'dict' and 'float'"
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.assertEqual(self.calculator.nth_root({'color': "1", 'blue': "1"}, 1), 0)

    def test_calc_root_str_and_float(self):
        error_message = "unsupported operand type(s) for ** or pow(): 'str' and 'float'"
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.assertEqual(self.calculator.nth_root("1", 1), 0)

    def test_calc_root_set_and_float(self):
        error_message = "unsupported operand type(s) for ** or pow(): 'set' and 'float'"
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.assertEqual(self.calculator.nth_root({"1"}, 1), 0)

    def test_calc_root_tuple_and_float(self):
        error_message = "unsupported operand type(s) for ** or pow(): 'tuple' and 'float'"
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.assertEqual(self.calculator.nth_root(("1", "1", 0), 1), 0)

    def test_calc_root_dict_and_float_2(self):
        error_message = "unsupported operand type(s) for ** or pow(): 'dict' and 'float'"
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.assertEqual(self.calculator.nth_root({'color': "1", 'blue': "1"}, 1), 0)

    def test_calc_root_negative_int(self):
        self.assertEqual(self.calculator.nth_root(-10233, 1), -10233.0)

    def test_calc_root_int_and_int_2(self):
        self.assertEqual(self.calculator.nth_root(1, 1), 1)

    def test_calc_root_int_and_int_3(self):
        self.assertEqual(self.calculator.nth_root(123, 213), 1.022849556248203)

    def test_calc_root_int_and_int_4(self):
        self.assertEqual(self.calculator.nth_root(2,2), 1.4142135623730951)

    def test_calc_degree_int_and_int(self):
        self.assertEqual(self.calculator.degree(2,2), 4)

    def test_calc_degree_int_and_negative(self):
        self.assertEqual(self.calculator.degree(2, -2), 0.25)

    def test_calc_degree_int_and_zero(self):
        self.assertEqual(self.calculator.degree(2, 0), 1)

    def test_calc_degree_int_and_str(self):
        error_message = "unsupported operand type(s) for ** or pow(): 'int' and 'str'"
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.assertEqual(self.calculator.degree(1, "1"), 0)

    def test_calc_degree_int_and_set(self):
        error_message = "unsupported operand type(s) for ** or pow(): 'int' and 'set'"
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.assertEqual(self.calculator.degree(1, {"1"}), 0)

    def test_calc_degree_int_and_tuple(self):
        error_message = "unsupported operand type(s) for ** or pow(): 'int' and 'tuple'"
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.assertEqual(self.calculator.degree(1, ("1", "1", 0)), 0)

    def test_calc_degree_int_and_dict(self):
        error_message = "unsupported operand type(s) for ** or pow(): 'int' and 'dict'"
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.assertEqual(self.calculator.degree(1, {'color': "1", 'blue': "1"}), 0)

    def test_calc_degree_dict_and_int(self):
        error_message = "unsupported operand type(s) for ** or pow(): 'dict' and 'int'"
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.assertEqual(self.calculator.degree({'color': "1", 'blue': "1"}, 1), 0)

    def test_calc_degree_str_and_int(self):
        error_message = "unsupported operand type(s) for ** or pow(): 'str' and 'int'"
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.assertEqual(self.calculator.degree("1", 1), 0)

    def test_calc_degree_set_and_int(self):
        error_message = "unsupported operand type(s) for ** or pow(): 'set' and 'int'"
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.assertEqual(self.calculator.degree({"1"}, 1), 0)

    def test_calc_degree_tuple_and_int(self):
        error_message ="unsupported operand type(s) for ** or pow(): 'tuple' and 'int'"
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.assertEqual(self.calculator.degree(("1", "1", 0), 1), 0)

    def test_calc_degree_dict_and_int_2(self):
        error_message = "unsupported operand type(s) for ** or pow(): 'dict' and 'int'"
        escaped_error_message = re.escape(error_message)
        with self.assertRaisesRegex(TypeError, escaped_error_message):
            self.assertEqual(self.calculator.degree({'color': "1", 'blue': "1"}, 1), 0)

    def test_calc_degree_int_and_negative_2(self):
        self.assertEqual(self.calculator.degree(2, -0.5), 0.7071067811865476)

    def test_calc_degree_negative_and_int(self):
        self.assertEqual(self.calculator.degree(-0.5, 2), 0.25)


if __name__ == "__main__":
    unittest.main()
