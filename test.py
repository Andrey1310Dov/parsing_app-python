import unittest
from parsing_app.function import search_id, search_login, search_sender, search_recipient, search_sent, remove_id

string_1 = 'search_id(Jul 10 10:09:08 srv24-s-st postfix/qmgr[3043]:25E6CDF04F4: from=<krasteplokomplekt@yandex.ru>, size=617951, nrcpt=1 (queue active)'
string_2 = 'Jul 10 10:09:32 srv24-s-st postfix/smtpd[10620]: 74A3FDF0502: client=unknown[213.87.122.107], sasl_method=LOGIN, sasl_username=manager30@moda-milena.ru'
string_3 = 'Jul 10 10:09:33 srv24-s-st postfix/qmgr[3043]: 0A2E9DF04FD: from=<m.kichigin@smobile-service.ru>, size=343400, nrcpt=1 (queue active)'
string_4 = 'Jul 10 10:09:20 srv24-s-st postfix smtp[22635]: F1DB8DF04EF:to=<ninachekmeneva@mail.ru> relay=mxs.mail.ru[94.100.176.20]:25, delay=1.3, delays=0.\
            76/0/0.02/0.49, dsn=2.0.0, status=sent (250 OK id=1SoTcu-0003aF-80)'
string_5 = 'Jul 10 10:09:36 srv24-s-st postfix/smtp[22621]: 0A2E9DF04FD: to=<zayavka@srsc.ru>, relay=mail.srsc.ru[212.44.145.132]:25, delay=7.9, delays=4.7/0/0\
            .02/3.1, dsn=2.6.0, status=sent (250 2.6.0 <597328317.20120710100842@smobile-service.ru> Queued mail for delivery)'
string_6 = 'Jul 10 10:09:30 srv24-s-st postfix/qmgr[3043]: 64C08DF04EF: removed'

 
class FunctionTest(unittest.TestCase):
    
    def test_search_id(self):
        self.assertEqual(search_id(string_1), '25E6CDF04F4')
        
    def test_search_login(self):
        self.assertEqual(search_login(string_2), '74A3FDF0502')
        
    def test_search_sender(self):
        self.assertEqual(search_sender(string_3), 'm.kichigin@smobile-service.ru')
        
    def test_search_recipient(self):
        self.assertEqual(search_recipient(string_4), 'ninachekmeneva@mail.ru')

    def test_search_sent(self):
        self.assertEqual(search_sent(string_5), 'sent')

    def test_remove_id(self):
        self.assertEqual(remove_id(string_6), '64C08DF04EF')
        
if __name__ == '__main__':
    unittest.main()
