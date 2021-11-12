// descriptive statistics
asdoc sum lnprice tensecu keyschool hospital metro sez fee nearctdis totalfloor, save(des_result.doc) replace dec(2)
asdoc sum lnprice keyschool hospital metro sez fee nearctdis totalfloor, by(tensecu) save(des_result.doc) dec(2)

// OLS regression
asdoc reg lnprice tensecu keyschool hospital metro,robust save(ols_result_3.doc) nest replace dec(3)
asdoc reg lnprice tensecu keyschool hospital metro sez fee nearctdis totalfloor,robust save(ols_result_3.doc) nest append dec(3)

// grouped regression
asdoc reg lnprice keyschool hospital metro sez fee nearctdis totalfloor if tensecu==0,robust save(ols_result_group.doc) nest replace dec(3)
asdoc reg lnprice keyschool hospital metro sez fee nearctdis totalfloor if tensecu==1,robust save(ols_result_group.doc) nest append dec(3)

// interaction term
asdoc reg lnprice tensecu##c.keyschool tensecu##c.hospital tensecu##c.metro sez fee nearctdis totalfloor, robust save(interact_result.doc) nest replace dec(3)
asdoc reg lnprice tensecu##c.keyschool sez fee nearctdis totalfloor, robust save(interact_result.doc) nest append dec(3)
asdoc reg lnprice tensecu##c.hospital sez fee nearctdis totalfloor, robust save(interact_result.doc) nest append dec(3)
asdoc reg lnprice tensecu##c.metro sez fee nearctdis totalfloor, robust save(interact_result.doc) nest append dec(3)

// asdoc reg lnprice tensecu##c.sez totalfloor fee nearctdis, robust save(interact_result.doc) nest append dec(2)
// asdoc reg lnprice tensecu##c.sez totalfloor fee nearctdis, robust save(interact_result.doc) nest append dec(2)

// SARAR model (带空间误差项的空间自回归模型)
// spset property_id,coord(lng lat)
// spset, modify coordsys(latlong,kilometers)
// spmatrix create idistance W, normalize(row) replace
// asdoc spregress lnprice hospital metro park tensecu sez totalfloor fee nearctdis ,gs2sls dvarl(W) errorl(W) het nest replace save(spatial_reg.doc) dec(2)
// asdoc spregress lnprice hospital metro park tensecu sez totalfloor fee nearctdis ,gs2sls dvarl(W) errorl(W) het nest append save(spatial_reg.doc) dec(2)
