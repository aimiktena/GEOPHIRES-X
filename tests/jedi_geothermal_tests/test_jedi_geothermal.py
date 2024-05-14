from base_test_case import BaseTestCase
from jedi_geothermal import JediGeothermalClient
from jedi_geothermal import JediGeothermalInputParameters
from jedi_geothermal import JediGeothermalResult


class JediGeothermalTest(BaseTestCase):

    def test_basic_example(self):
        client = JediGeothermalClient()

        input_params = JediGeothermalInputParameters()
        input_params.resource_depth_m = 2250
        # TODO define rest of input_params properties

        result: JediGeothermalResult = client.get_jedi_geothermal_result(input_params)
        self.assertIsNotNone(result)

        # TODO assert result properties are calculated from inputs correctly
        # i.e.
        # self.assertEqual(183, result.construction_period_total_jobs)
        # self.assertEqual(1.70, result.operating_years_annual_value_added_MUSD)
        # etc.
