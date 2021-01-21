""""
Briefly it tests whether the found minimum and maxiumum distances
is equal to the pre-determined output The second test tests
if the input features have equal distances to each other,
will the tests give the expected output.

"""
class SaveAttributesDialogTest(unittest.TestCase):
    """Test dialog works."""
    @classmethod
    def setUpClass(cls):
        cls.iface = get_iface()
        cls.vlayer = QgsVectorLayer(test_data_folder()+'/test_data_point.shp', 'test_data', "ogr")
        cls.instance = SaveAttributes(cls.iface)
        
    def setUp(self):
        """Runs before each test."""
        QgsProject.instance().clear()
        self.dialog = SaveAttributesDialog(None)

    def test_find_min_max_distance(self):
        minDist = self.instance.find_min_max_distance(self.vlayer)
        self.assertEqual(minDist, [19.370555303797016, 25.27174091573615])

        equalPointsLayer = QgsVectorLayer("point", "eq_point","memory")
        equalPointsLayer.startEditing()
        pr = equalPointsLayer.dataProvider()

        pointFeatures = []
        for i in range(3):
            pointFeature = QgsFeature()
            pointFeature.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(10,10)))
            pointFeatures.append(pointFeature)
        pr.addFeatures( pointFeatures )
        equalPointsLayer.updateExtents()
        equalPointsLayer.commitChanges()
        
        minDistSamePoint = self.instance.find_min_max_distance(equalPointsLayer)
        self.assertEqual(minDistSamePoint, False)
        

    def tearDown(self):
        """Runs after each test."""
        self.dialog = None
    
  

if __name__ == "__main__":
    suite = unittest.makeSuite(SaveAttributesDialogTest)
    runner = unittest.TextTestRunner(verbosity=2)
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    runner.run(suite)
