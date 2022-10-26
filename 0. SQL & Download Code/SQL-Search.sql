/*

SDSS SQL Search :
http://skyserver.sdss.org/dr17/SearchTools/sql

SDSS SkyServer Exploere :
http://skyserver.sdss.org/dr17/VisualTools/explore/summary

SDSS Visual Tools List :
http://skyserver.sdss.org/dr17/VisualTools/list

*/

---------- 22. 10. 26. SQL ----------

--- Skyserver_SQL_221026_STAR_177374_Mag10to17
SELECT
s.class, p.ObjID, p.ra, p.dec, s.z, p.modelMag_u, p.modelMag_g, p.modelMag_r, p.modelMag_i, p.modelMag_z
FROM
PhotoObj p
JOIN specObj s ON s.bestObjID=p.objID
WHERE
p.modelMag_r BETWEEN 10.00 AND 16.99
AND s.class = 'STAR'

--- Skyserver_SQL_221026_STAR_451307_Mag17to20
SELECT
s.class, p.ObjID, p.ra, p.dec, s.z, p.modelMag_u, p.modelMag_g, p.modelMag_r, p.modelMag_i, p.modelMag_z
FROM
PhotoObj p
JOIN specObj s ON s.bestObjID=p.objID
WHERE
p.modelMag_r BETWEEN 17.00 AND 20.00
AND s.class = 'STAR'

----------------------------------------

--- Skyserver_SQL_221026_GALAXY_334480
SELECT
s.class, p.ObjID, p.ra, p.dec, s.z, p.modelMag_u, p.modelMag_g, p.modelMag_r, p.modelMag_i, p.modelMag_z
FROM
PhotoObj p
JOIN specObj s ON s.bestObjID=p.objID
WHERE
s.z BETWEEN 0.02 AND 0.10
AND p.modelMag_r BETWEEN 10.00 AND 30.00
AND s.class = 'GALAXY'