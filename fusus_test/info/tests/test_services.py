import responses
from ..import services
from django.test import TestCase



class InfoServiceTestCase(TestCase):

    def setUp(self):
        self.responses = responses.RequestsMock()
        self.responses.start()
        self.addCleanup(self.responses.stop)
        self.addCleanup(self.responses.reset)

    def test_api_returns_ip_on_suceess(self):
        public_ip = '172.12.43.23'
        self.responses.add(
            responses.Response(
                method='GET',
                url=services.IP_CHECK_URL,
                status=200,
                content_type='text/plain',
                body=f'{public_ip}\n'
            )
        )
        self.assertEqual(services.get_public_ip(), public_ip)

    def test_api_returns_unknown_on_failure(self):
        self.responses.add(
            responses.Response(
                method='GET',
                url=services.IP_CHECK_URL,
                status=400,
                content_type='text/plain',
            )
        )
        self.assertEqual(services.get_public_ip(), 'unknown')
