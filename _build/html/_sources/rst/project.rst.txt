PROJECT DESCRIPTION
======================

|nbspc| |nbspc| Hello everyone! We have created and contributed new features to a **QGIS plugin** called |br| **"Save Attributes"**. You may find a brief information about the plugin below.  

.. |nbspc| unicode:: U+00A0 .. non-breaking space

Interface & Features
-------------------------   
.. figure:: /image/GUI.png

|nbspc| You could select the shapefile from the interface (Input layer part). And there will be 3 main cases:

Case 1
^^^^^^^^
  If the input layer geometry is line; the plugin will compute the shortest and real distance among features, azimuth and reverse azimuth between lines' start points and end points. And also draw the shortest line with its length. See below,  
.. figure:: /image/line_1feat.jfif
.. figure:: /image/lines_attr.jfif
|br| 
  If there is more than one feature on layer. It will also show the features which could possibly be a polygon.    
.. figure:: /image/line_mult.jfif
.. figure:: /image/azimuth.png

Case 2
^^^^^^^^^^
  If the input layer is point. It will check whether feature number is greater than 2. If it is the case, it  will calculate the minimum and maxiumum distannce among all points and draw the lines related to them. See below,      
.. figure:: /image/minmax.jfif
.. figure:: /image/point_attr.jfif

Case 3
^^^^^^^^^^^^^
  If the input layer is polygon, the plugin computes the area and perimeter of the poligons and show in the table with inserting.
.. figure:: /image/area-peri.png

|br| 
|br| 
*Note*: We used this to be able to add our university logo to the GUI: https://gis.stackexchange.com/questions/381661/image-adding-problem-to-qgis-plugin-gui-with-qt-designer (You may need to run the "compile.bat" file in the folder according to you for the logo.)


Usage Video
--------------------------------

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/pJdj8PcLHI4" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
|br|   

Supported Languages
---------------------------------
* |eng| **English** 	|br|
* |tur| **Türkçe**  	|br|
* |deu| **Deutsche**	|br|
* |esp| **Española**	|br|
* |rus| **русский**		|br|

.. |eng| image:: /image/eng.png
   :scale: 25 %
.. |tur| image:: /image/tur.png
   :scale: 25 %
.. |deu| image:: /image/deu.png
   :scale: 25 %
.. |esp| image:: /image/esp.png
   :scale: 25 %
.. |rus| image:: /image/rus.png
   :scale: 25 %
|nbspc| |nbspc| You can choose any of the supported languages from the QGIS settings and use the graphical user interface with the language of your choice.
  
.. figure:: /image/lang1.png
   :align: center
   
   Spanish GUI

|nbspc| |nbspc| We used **Qt Linguist** software while translating languages. If you want to add your own language to the plugin, you can provide translation with Qt Linguist. |qtl| 
  
.. image:: /image/lang2.png

.. |qtl| image:: /image/qtlin.jpg
   :scale: 20 %
|br|    

Authors & Contact
------------------

========================  ============================
   Author     			   Contact
========================  ============================
Ahmet Fırat Karaoğlu  	  karaoglu@email.com
Metehan Ergen  			  metehan.ergenn@gmail.com
========================  ============================
|br|
|br|
:ref:`Homepage <home>`



			 
.. |br| raw:: html

  <br/>


