class ContactTests(TestCase):
    """Contact model tests"""
    
    def test_str(self):
        contact = Contact(first_name='john', last_name='smith')

        self.assertEquals(
		    str(contact), 'john smith'
        )
