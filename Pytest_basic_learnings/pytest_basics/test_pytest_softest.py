import softest


class Test(softest.TestCase):

    def test1_exe(self):
        #self.soft_assert(self.assertEqual(self,10,9))
        #self.soft_assert(self.assertEqual(self,10,9))
        self.soft_assert(self.assertTrue, True)
        self.soft_assert(self.assertTrue, False)
