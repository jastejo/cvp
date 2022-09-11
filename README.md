# cvp
                                                     Hydrograph and Unit Hydrograph


Hydrograph shows graphical representation of discharge or flow data on the river as function of time. The discharge is plotted as Y-axis and time series data (hourly, daily or monthly basis) is presented in X-axis. Commonly, Hydrograph is used as tool to interpret the response of watershed due to rainfall events. Hydrograph composed of two components, i.e.: Surface runoff and base flow. Surface runoff represent the rapid response of the river on the watershed caused by direct surface runoff. Base flow represent the response of the river on the watershed supplied by groundwater flow and other type of flow that enter more slowly to the river streams. Estimation of base flow and direct runoff is useful to understand the hydrology of a watershed, including interaction of surface and sub-surface water
                      Base flow separation is often used to determine what portion of a streamflow   hydrograph occurs from base flow, and what portion occurs from overland flow. The surface runoff hydrograph obtained after the base-flow separation is also known as direct runoff hydrograph (DRH).
Definition of Unit Hydrograph:
It is a typical hydrograph of direct runoff which gets generated from one centimeter of effective rainfall falling at a uniform rate over the entire drainage basin uniformly during a specific duration. Effective rainfall is that portion of rainfall which fully contributes towards direct runoff. Therefore, unit hydrograph can also be defined as the hydrograph of a drainage basin which gives one centimeter of direct runoff from a rain storm of specific duration.
The main assumptions for Unit Hydrograph are following:
(i) The effective rainfall is uniformly distributed over the entire drainage basin.
(ii) The effective rainfall occurs uniformly within its specifier duration.
This requirement calls for selection of storms of so small a duration which would generally produce an intense and nearly uniform effective rainfall and would produce a well-defined single peak of hydrograph of short time base. Such a storm can be termed as “unit storm”.
(iii) The ordinates of the direct runoff hydrographs having same time base (i.e., hydrographs due to effective rainfalls of different intensity but equal duration) are directly proportional to the total amount of direct runoff given by each hydrograph. This important assumption is called principle of linearity or proportionality or superposition.
(iv) The hydrograph of runoff from a given drainage basin resulting, from a given pattern of rainfall reflects all the combined physical characteristics of the basin. In other words the hydrograph of direct runoff resulting from a given pattern of effective rainfall will remain invariable irrespective of its time of occurrence. This assumption is called principle of time invariance.
Limitations of Unit Hydrograph Theory:
 In theory, the principle of unit hydrograph is applicable to a drainage basin of any size. In practice, however, uniformly distributed effective rainfall rarely occurs on large areas. Also on large areas effective rainfall is very rarely uniform at all locations, within its specified duration. Obviously bigger the area of the drainage basin lesser will be the chances of fulfilling the assumptions enunciated above. The limiting size of the drainage basin is considered to be 5000 km2. Beyond it the reliability of the unit hydrograph method diminishes.
 
 Reservoir Flood Routing
Introduction
 A flood is an unusually high stage in a river – normally the level at which the river overflows its banks and inundates the adjoining area. The damages caused by floods in terms of loss of life, property and economic loss due to disruption of economic activity are very high. Flood peak values are required in the design bridges, culvert waterways, spillways for dams, and estimation of scour at a hydraulic structure.
Reservoir flood routing using Modified pulse method
As the horizontal water surface is assumed in the reservoir, the storage routing is also known as Level Pool Routing.
The reduction in the peak of the outflow hydrograph due to storage effects is called attenuation. Further the peak of outflow occurs after the peak of the inflow; the time difference between the peaks of inflow and outflow hydrographs is known as lag. Modification in the hydrograph is studied through flood routing. Flood routing is the technique of determining the flood hydrograph at a section of a river by utilizing the data of flood flow. 
                The continuity equation used in reservoir routing observes the principle of conservation of mass.   For a given time, interval, the volume of inflow minus the volume of outflow equals the change in volume of storage. 
 The computations are performed as follows. At the starting of flood routing, the initial storage and outflow discharge are known.
 (I1 + I2) ∆t/2 – (Q1 + Q2) ∆t/2 = S2 – S1    
The above Equation can be rearranged as below: 
(I1 + I2) ∆t/2 + (S1 – Q1∆t/2) = (S2 + Q2 ∆t/2)    Equation (1)
In equation (1) all the terms in the left hand side are known at the beginning of time step ∆t. Hence the value of the function (S2 + Q2 ∆t/2) at the end of the time step is calculated. Since the relation S = S(h) and Q = Q(h) are known, (S2 + Q2 ∆t/2) will enable one to determine the reservoir elevation and hence the discharge at the end of the time step. The procedure is repeated till the entire inflow hydrograph is routed. From the known Storage-Elevation and Discharge-Elevation data, prepare a curve of (S + Q ∆t/2) and a curve of outflow discharge –elevation Here ∆t is approximately 20 to 40% of the time of rise of the inflow hydrograph.

Channel routing by Muskingum method
The Muskingum method is a hydrological flow routing model with lumped parameters, which describes the transformation of discharge waves in a river bed using two equations. The first one is the continuity equation (conservation of mass) and the second equation is the relationship between the storage, inflow, and outflow of the reach (the discharge storage equation). These equations are applied within a river reach between two cross sections of a river. The parameters of the model can be estimated by several method
Estimate  of Parameters K and X  
The Muskingum K parameter is equivalent to the travel time through the reach. The Muskingum X parameter is a dimensionless coefficient that lacks a strong physical meaning.  This parameter must range between 0.0 (maximum attenuation) and 0.5 (no attenuation).  When this parameter is set to a value of 0, storage within the reach is computed solely as a function of outflow.  This is equivalent to level pool routing and results in the maximum possible amount of attenuation.  When this parameter is set to a value of 0.5, equal weight is given to both inflow and outflow when determining storage within the reach.  This results in no attenuation to the inflow hydrograph as it progresses through the reach.  For most applications, an initial estimate of 0.25 is further refined through model calibration.

LONGITUDINAL SECTION OF RIVER OF VAMASADHARA:
LONGITUDINAL SECTION OF RIVER OF VAMASADHARA is prepared using excel data file  and SWDTM software.


 


