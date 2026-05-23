## TABLE OF CONTENTS

1. **INTRODUCTION** ....................................................................................................4
   - 1.1 SCOPE..............................................................................................................4
   - 1.2 DISTRIBUTION, INTENDED USE AND REGULATORY CONSIDERATIONS .......4
   - 1.3 DEFINITIONS ....................................................................................................4
   - 1.4 CROSS-REFERENCES .....................................................................................6

2. **GENERAL DESIGN ASPECTS**..............................................................................7
   - 2.1 INTRODUCTION ...............................................................................................7
   - 2.2 TYPES OF SLUG CATCHER .............................................................................7

3. **HYDRAULIC DESIGN** ...........................................................................................9
   - 3.1 GENERAL .........................................................................................................9
   - 3.2 SLUG CATCHER SIZE ....................................................................................11
   - 3.3 SLUG CATCHER GEOMETRY AND COMPONENTS........................................13
   - 3.4 LIQUID OUTLET HEADER..............................................................................16
   - 3.5 LIQUID LEVEL INDICATION AND CONTROL..................................................17
   - 3.6 RECOMMENDED SEQUENCE OF CALCULATION..........................................18

4. **MECHANICAL DESIGN** ......................................................................................19
   - 4.1 GENERAL .......................................................................................................19
   - 4.2 MAXIMUM ALLOWABLE OPERATING PRESSURE.........................................19
   - 4.3 DESIGN FACTOR FOR HOOP STRESS..........................................................19
   - 4.4 OTHER STRESS .............................................................................................19
   - 4.5 SUPPORTS AND ANCHORS ...........................................................................19
   - 4.6 MATERIAL SELECTION..................................................................................20
   - 4.7 WELDING ........................................................................................................20
   - 4.8 INTERNAL/EXTERNAL CORROSION PROTECTION ......................................20
   - 4.9 OVERPRESSURE PROTECTION ....................................................................20
   - 4.10 MAINTENANCE ............................................................................................21
   - 4.11 EMERGENCY DEPRESSURISATION ............................................................21

5. **HAZARD AND RISK MANAGEMENT** .................................................................22
   - 5.1 OBJECTIVE.....................................................................................................22
   - 5.2 HAZARD AND RISK MANAGEMENT ASSESSMENT.......................................22
   - 5.3 LOSS OF CONTAINMENT ..............................................................................22
   - 5.4 ESCALATION SCENARIOS ............................................................................22
   - 5.5 DESIGN CONSIDERATIONS ..........................................................................22

6. **REFERENCES** ....................................................................................................24

7. **FIGURES** .............................................................................................................25

## APPENDICES

APPENDIX 1    LIQUID STORAGE CAPACITY OF A MULTIPLE-PIPE SLUG CATCHER ...38

APPENDIX 2    SEPARATION OF LIQUID DROPS IN A PRIMARY BOTTLE.......................39

# 1. INTRODUCTION

## 1.1 SCOPE

This new DEP specifies requirements and gives recommendations for the design of multiple-pipe slug catchers to be installed on land. Vessel-type slug catchers and parking loop slug catchers are only briefly described.

## 1.2 DISTRIBUTION, INTENDED USE AND REGULATORY CONSIDERATIONS

Unless otherwise authorised by SIOP and SIEP, the distribution of this DEP is confined to companies forming part of the Royal Dutch/Shell Group or managed by a Group company, and to Contractors and Manufacturers/Suppliers nominated by them (i.e. the distribution code is "F", as described in DEP 00.00.05.05-Gen.).

This DEP is intended for use in gas plants, exploration and production facilities and supply/marketing installations.

If national and/or local regulations exist in which some of the requirements may be more stringent than in this DEP, the Contractor shall determine by careful scrutiny which of the requirements are the more stringent and which combination of requirements will be acceptable as regards safety, environmental, economic and legal aspects. In all cases the Contractor shall inform the Principal of any deviation from the requirements of this DEP which is considered to be necessary in order to comply with national and/or local regulations. The Principal may then negotiate with the Authorities concerned with the object of obtaining agreement to follow this DEP as closely as possible.

## 1.3 DEFINITIONS

### 1.3.1 General definitions

The **Contractor** is the party which carries out all or part of the design, engineering, procurement, construction, commissioning or management of a project, or operation or maintenance of a facility. The Principal may undertake all or part of the duties of the Contractor.

The **Manufacturer/Supplier** is the party which manufactures or supplies equipment and services to perform the duties specified by the Contractor.

The **Principal** is the party which initiates the project and ultimately pays for its design and construction. The Principal will generally specify the technical requirements. The Principal may also include an agent or consultant authorised to act for, and on behalf of, the Principal.

The word **shall** indicates a requirement.

The word **should** indicates a recommendation.

### 1.3.2 Specific definitions terms of slug catcher parts

**Bottle, primary** — Pipe-type part of a multiple-pipe slug catcher for separation of the fluid and storage of the liquids, sloping down under small angle(s) from the lower end of the downcomer (see Figure 3).

**Bottle, secondary** — Pipe-type part of a multiple-pipe slug catcher for storage of the liquids only, sloping down towards the liquid outlet header (see Figure 3).

**Downcomer** — Vertical or steeply sloping pipes of a multiple-pipe slug catcher between the inlet header and the primary bottles (see Figure 3).

**Equalizer** — A header interconnecting the bottles of a multiple-pipe slug catcher

catcher for the purpose of equalizing the pressure in the various bottles of the slug catcher (see Figure 3).

**Gas outlet header**
Part of a multiple-pipe slug catcher on top of and connecting all risers for collection of the out going gas streams (see Figure 3).

**Inlet header**
Part of a multiple-pipe slug catcher in which the fluid is evenly distributed before entering the downcomers and in which fluid flow conditions are further improved for separation (see Figure 3). Also called distribution header.

**Liquid outlet header**
The lowest part of the multiple-pipe slug catcher, in which the liquid is collected for export (see Figure 3). Also called liquid header.

**Gas riser**
Vertical pipe on top of a bottle, through which gas exits (see Figure 3).

**Separator**
Equipment for separating gas and liquids or various liquids of a mixed fluid.

**Slug catcher**
Part of a gas pipeline system for separation of the gas and liquid phases and for temporary storage of the liquids.

**Slug catcher, multiple-pipe type**
Slug catcher, made of pipe material.

**Slug catcher, parking loop type**
Slug catcher, where the separator is located apart from the storage part. The separator can be a vessel type and the storage part is made of pipeline material, which can be located away from the separator (see Figure 7).

**Slug catcher, vessel type**
Slug catcher of limited dimensions and capacity, where separator and storage parts are combined within one or a combination of vessels (see Figure 1).

**Splitter**
Inlet of a multiple-pipe slug catcher in which the fluid stream is split up for even distribution over the inlet header. (see Figure 2 and Figure 3).

## 1.3.3 Symbols

| Symbol | Description |
| :--- | :--- |
| Cw | drag coefficient |
| d | diameter of droplet (m) |
| D | diameter (m) |
| H | hold-up fraction |
| g | gravity constant (m/s²) |
| L | length (m) |
| m | number of risers per bottle |
| n | number of bottles |
| V | velocity (m/s) |
| Vol | volume (m³) |
| Q | gas flow rate (m³/s) |
| Re | Reynolds number |

**Greek symbols**

η	dynamic viscosity (N.s/m²)

λ	load factor (m/s)

	or

	volumetric fraction of liquid in two-phase flow

θ	angle between bottle and horizontal plane

ρ	density (kg/m³)

**Subscripts**

b	bottle

buffer	buffer

loh	liquid outlet header

G	gas

int	intercept

L	liquid

goh	gas outlet header

pb	primary bottle

pipeline	pipeline

s	settle

sb	secondary bottle

SC	slug catcher

SG	superficial gas

SL	superficial liquid

### 1.3.4 Abbreviations

D$_{bottle}$	internal diameter of the multiple-pipe slug catcher bottles

D$_{downcorner}$	internal diameter of the downcorner

D$_{goh}$	internal diameter of the gas outlet header

D$_{outlet}$	internal diameter of the gas outlet

D$_{riser}$	internal diameter of the gas risers

DP	differential pressure

MAOP	maximum allowable operating pressure

SMYS	specified minimum yield strength

SGV	sphere-generated volume

## 1.4 CROSS-REFERENCES

Where cross-references to other parts of this DEP are made, the referenced section number is shown in brackets. Other documents referenced in this DEP are listed in (6) and (7).

## 2. GENERAL DESIGN ASPECTS

### 2.1 INTRODUCTION

A two-phase flow pipeline is intended for transporting the gas and liquid phases simultaneously. The slug catcher situated at the end of the pipeline is intended to separate the phases and to provide temporary storage for the liquid received. There are different modes under which liquid can be produced from the pipeline. These include: the continuous liquid flow production mode under normal steady flow conditions; the intermittent or transient liquid production mode occurring when flow rates are varied; and the pigging or sphering mode when liquid is displaced from the pipeline into the slug catcher in a relatively short time.

In the past ten years, the range of application of two-phase pipeline transportation has broadened considerably. Conditions under which slug catchers are required to operate have extended to higher flowrates involving also mist and droplet flow conditions for which more stringent separation requirements have become necessary and in some cases very large liquid quantities have to be handled.

This DEP has combined existing design approaches with results based on an additional investigation of liquid separation under high velocity conditions so that the revised design requirements can be met. In the new approach, the function of separation at high flow velocities in a multiple-pipe slug catcher is assigned to the horizontal parts of primary bottles before the gas risers. In the previous approach, the gas risers had to be sized to prevent liquid carry-over at the highest flow rate; with the new approach they have to be sized only to prevent carry-over during pig arrivals which occur at lower flow conditions and when the slug catcher may be nearly full. The result of the different approach will be that the section of primary bottles required for liquid separation will be longer, compared to some older models, while the need for excessively large gas risers can be avoided.

### 2.2 TYPES OF SLUG CATCHER

Slug catchers can be broadly classified into the three following categories:

1. vessel type;
2. multiple-pipe type;
3. parking-loop type.

#### 2.2.1 Vessel-type slug catcher

The geometry of the vessel-type slug catcher could range from a simple knock-out vessel to a more sophisticated lay-out (Figure 1). Since the overall length of vessel-type slug catchers is relatively short for a given volume this type is often preferred in the case of limited plot sizes (e.g. offshore platforms). When larger liquid volumes have to be accommodated, say of more than 100 m³, either the multiple-pipe or the parking-loop type should be used.

#### 2.2.2 Multiple-pipe slug catcher

Examples of typical multi-pipe slug catchers are shown in Figures 2, 3, 4 and 5.

Multi-pipe slug catchers can be made of standard pipeline materials. Besides having a cost advantage over the high-pressure vessel design, this type allows for a greater flexibility in design possibilities to cope with wide ranges of flow conditions and geometrical configurations with different shapes of the available ground area.

A definition and description of the main parts of this type of slug catcher is given in (1:3.2). More information concerning their specific hydraulic function is given in (3).

In general (see Figure 4 for example), multi-pipe slug catchers have a flow scheme as follows. Immediately at the inlet is a splitter to feed the two-phase stream into the inlet header from which connections are open to downcomer(s) leading to bottle (primary bottle). The primary bottle diameter is usually of a larger size than the downcomer in order to

reduce flow velocity. The first section of a primary bottle up to the gas riser is intended to allow for liquid settling and separation. The remaining part is intended for liquid storage. Gas present in the bottles is displaced through the gas risers to the gas outlet header. This shunting action of the liquid and gas phases in the bottles assures an uninterrupted gas supply to downstream facilities during liquid slug arrival.

The advantage of a multiple-pipe slug catcher is that it is easy to operate since no flow controls are required. One disadvantage, however, is the counter-current gas-liquid flow in the bottles which may promote liquid carry-over if it is incorrectly designed.

## 2.2.3 Parking loop slug catcher

In this DEP the parking-loop slug catcher is only mentioned for general information.

The problem of counter-current flow is avoided in the parking-loop type slug catcher. This concept is illustrated in Figure 7. In this concept the separating and storage parts are virtually disconnected: it consists basically of a large separator with the liquid outlet connected to a long single pipe-loop. The incoming gas/liquid stream is separated in the vessel. When the liquid level rises rapidly, indicating that a slug rather than a gas-liquid mixture is arriving, gas flow from the vessel is restricted forcing the liquid to flow into the pipe-loop in which a sphere separates the liquid entering from the gas present. With the other end of the loop now opened to the downstream facilities the gas is driven out in a direct co-current manner. The stored (parked) liquid can be discharged as a single slug by using high pressure gas if the location is at a booster compressor station as shown in Figure 7 or the liquid can be discharged gradually to a downstream treating plant. This type of slug catcher is particularly suited to offshore applications where the separator can be placed on the platform and the parking loop on the sea-bed. All valves and controls would be on the platform. The advantage of the concept is the possibility to save space. A disadvantage of the method is the high reliance on strict operational procedures.

## 3. HYDRAULIC DESIGN

### 3.1 GENERAL

Guidelines for the hydraulic design of different parts of a multiple-pipe slug catcher are preceded in this section by a description of the important hydraulic function of a slug catcher, the separation of the gas and liquid phases.

The hydraulic design is based on theoretical and experimental work and field experience with existing slug catchers.

#### 3.1.1 Condition of liquid to be separated

There are several conditions under which the slug catcher has to perform as a separator, namely:

##### 3.1.1.1 Liquid arriving with sphere or pig

Depending on the condition before pigging, the quantity of liquid arriving can be large. The rate of liquid arrival is dictated by the speed of the pig, which may typically be between 2 and 5 m/s. As the liquid is separated from the gas by the pig or sphere, the amount of gas, either resulting from bubbles in the slug or flow bypassing the pig, will be relatively small and the mixture will generally be in the form of slug or bubble flow.

##### 3.1.1.2 Liquid arriving under steady flow condition

The ratio of liquid to gas arriving at the slug catcher will be the same as for the steady flow condition of the system and the liquid will be arriving at a continuous rate. It will be either in the form of entrained droplets, slugs or a steady stratified stream depending on gas/ liquid ratio, pipeline profile and the prevailing flow rate of the pipeline. If in the form of droplets, their sizes will be influenced by velocity and become smaller at higher velocities.

##### 3.1.1.3 Liquid produced as a result of flow rate increase

When the flow rate in the pipeline is being increased, the corresponding volume of liquid holdup under equilibrium will be reduced and the excess quantity will be displaced. It will arrive in the form of slugs or surges of droplets depending on the prevailing gas velocity. The instantaneous liquid-to-gas ratio at the outlet will be greater than the steady flow liquid-to-gas ratio.

#### 3.1.2 Separation mechanisms

In a slug catcher the separation of liquid from the gas can occur in different manners as follows:

1. Stratification in the inlet manifold, downcomer and primary bottle.
2. Droplet settling in the primary bottle.
3. Deposition in bends and primary bottle.
4. Tee-junction separation at inlet manifolds.
5. Tee-junction separation at entry into a gas riser.

(3.1.2.1 to 3.1.2.5) describe the above separation mechanisms.

##### 3.1.2.1 Stratification

Stratification is the flow pattern in which separation will happen. It generally occurs when velocity is reduced. This flow regime is encouraged to form when flowing over a declination. To create such conditions, the flow is often split into parallel passages of large diameter pipes. The passages are inclined downward whenever possible.

#### 3.1.2.2 Droplet settling

Setting of droplets can occur by gravitation in a primary bottle when flowing at low velocities, typically at less than 2 m/s, towards the gas riser, provided sufficient residence time is allowed for it to happen.

#### 3.1.2.3 Deposition in bends and first section of primary bottle

Settling velocity of a droplet decreases with its size so that smaller droplets need more time to settle. Therefore separation by settling due to gravity will become difficult at increased velocities. However, the effect due to turbulence at increased velocities can have a positive influence on the separation of smaller droplets. They tend to follow turbulent fluctuation paths, thus increasing the chances of collision with pipe walls for deposition. This can be expected to occur particularly in bends and when a downcomer expands into a primary bottle with the jet of flow impinging obliquely against a wall.

Figure 8 depicts separation efficiencies in a slug catcher as a function of droplet size. It was determined by means of the computational fluid dynamics code, "FLUENT", simulating droplet behaviour in a large slug catcher bottle of 1.22 m diameter with a 45 degree inclined downcomer of 0.9 m diameter. It can be seen that larger droplets separate better under the influence of gravity while the positive effect due to turbulence is noticeable for droplets smaller than 150 μm. Of particular interest is the significant effect due to impingement at the bend just downstream of the downcomer. The assumed shape of the droplet size distribution for this case is typical but practical data have revealed the maximum droplet size to be nearer 1000 μm than the 500 μm used in Figure 8.

#### 3.1.2.4 Tee-junction separation at inlet manifold

A downward inclined T-branch on a horizontal pipe can be an effective separator particularly if the mixture stream in the horizontal part is stratified. While the gas flow will continue in the horizontal direction, most of the liquid will separate and go through the branch. This is depicted in Figure 9.

#### 3.1.2.5 Tee-junction separation at entry to a riser

When the tee-branch on a horizontal pipe is oriented in the upward direction, e.g. the gas riser on a primary bottle, efficient separation will be possible provided less than 80% of the gas exits through that branch. Figure 10 depicts the measured separation performance of a riser in the laboratory. It shows that no liquid will be carried up the riser if not more than 80% of the gas flow is directed through it. Liquid in the horizontal pipe in the stratified pattern will continue in the horizontal direction. Entrained droplets will also continue with the remaining gas flow in the horizontal pipe. However, this separation tendency will be reduced when the gas flow through the riser is increased beyond 80% of the total. For this reason, two successive risers per primary bottle with a 70% / 30% gas flow distribution have been used in the recent design for the MLNG-2 slug catcher to utilise these special separation characteristics (see Figure 5).

## 3.2 SLUG CATCHER SIZE

The size of a slug catcher (Vol<sub>sc</sub>) is directly related to the maximum liquid volume it has to hold. It must be able to intercept the maximum possible slug size emerging from the two phase pipeline at any moment (Vol<sub>sl</sub>). It should also contain a buffer volume of condensate (Vol<sub>buffer</sub>) in order to guarantee liquid supply to treating facilities downstream of the slug catcher. Hence:

Vol<sub>sc</sub> = Vol<sub>sl</sub> + Vol<sub>buffer</sub>

The intercepting capacity of the slug catcher should allow for all modes of liquid production at the end of the pipeline. It is dependent on the maximum difference of liquid inflow from the pipeline and outflow to its downstream process. The time over which such liquid surges have to be coped with is determined by the nature and operating philosophy of the system.

For example, if the pipeline is to be sphered regularly, it can be sized according to the amount of liquid expected to accumulate between pigging intervals. For this operating scenario, the capacity of these liquid processing facilities should be based on slug volume, interval of pigging and a contingency volume. If pigging may be performed only occasionally, it will be necessary to know the lowest flow condition of the pipeline reached for a pigging operation. The required slug catcher size to cope with that corresponding maximum sphere-generated volume (SGV) of liquid can be calculated by the computer program "TWOPHASE" or an alternative program approved by the Principal. In the case that pigging does not need to be allowed for but sphere-shaped flows will be expected as a result of flow variation, the slug catcher should be sized to accommodate the differences between the steady state hold-up volumes predicted for the corresponding changes of flows.

For long pipelines, sphere-generated volumes (SGV) based on equilibrium hold-up conditions can be very large and a special operating and pigging philosophy may have to be devised to limit the size of a slug catcher. For unusual pipeline profiles which may generate terrain slugs or tend to produce liquid surges when starting up from standstill, the transient simulation program "TRAFLOW" may be needed for sizing the slug catcher.

Recent trials with by-pass pigs have shown that they can effectively reduce the liquid arrival rate at the slug catcher and extend the slug arrival period ahead of the pig. Therefore depending on the nature of the case being studied, it would be recommended to consider the use of by-pass pigs in order to reduce the size of the slug catcher required.

The size of Vol<sub>buffer</sub> is largely determined by the characteristics of the liquid-treatment facilities and required plant flexibility.

For a fully filled slug catcher, the maximum liquid level in a multi-pipe slug catcher should be at the point where the centreline of the last gas riser intersects with the bottom wall of the primary bottle (see Appendix 1, Figure 1-1). It can not be excluded that some liquid will be entrained into the gas riser at high velocity conditions in a fully filled slug catcher by some film entrainment effect. Instead of modifying design rules for the riser conservatively, the period of operating conditions involving high liquid levels in the slug catcher should be kept as short as possible, also for safety reasons.

## 3.3 SLUG CATCHER GEOMETRY AND COMPONENTS

### 3.3.1 Inlet section

The distribution of the incoming liquid over the bottles takes place in the inlet section. Here also, the gas/liquid separation begins by promoting the occurrence of stratified two-phase flow. This section comprises:

1. End of the pipeline
2. Splitter(s)
3. Inlet header
4. Constrictors
5. Downcomers
6. Expanders

To prevent unwanted acceleration of the gas/liquid mixture, the pipeline diameter should be maintained up to the inlet of the slug catcher.

For efficient filling and maximum utilisation of storage capacity of a multiple-pipe slug catcher, it is important to distribute gas and liquid flows equally between parallel bottles in the slug catcher. This can be achieved by splitters in the form of Tee-junctions, with the flow impacting perpendicularly at the tee-junction before being divided into equal streams departing through the runs. Tee-junctions are often arranged in series to divide and subdivide flow into 2, 4 and 8 equal and parallel streams. Passage areas are generally adjusted to maintain constant flow velocity and to create back pressure for even flow splitting.

Inlet manifolds are sometimes installed across the outlets of splitters (Figure 5). They should have a large diameter to help even out the phases before continuing through parallel downcomers. The number of downcomers per inlet manifold should be limited to eight. To ensure good distribution of the liquid at low flow rates but with large liquid fractions, e.g. when a sphered slug is arriving, constrictors can be placed at the beginning of each downcomer (Figure 2 and Figure 11). Each of these should provide passage passages of at most 40% or less of the inner diameter of the inlet header to guarantee an even liquid distribution. The constrictors should be located eccentrically and close to the wall on the lower side of the downcomer. In this way a jetting effect which could lead to excessive mist/foam generation is suppressed as the liquid is guided along the wall. In addition, dirt accumulation upstream of the constrictor is avoided. Instead of a constrictor welded to the inside of the downcomer, an expander with its flat side down beginning from an eccentric tee on the manifold should be used (Figure 4).

Segregation of gas and liquid is promoted as the stream is expanded downstream of the constrictor. This segregation could be further promoted by the selection of a down-comer ratio of 1:1 rather than using vertical downcomers. It has been found that an angle of 45° with the horizontal plane is optimal for the development of stratified flow.

In existing slug catchers the diameter of the downcomers is smaller than that of the bottle header arbitrarily: D*downcomer* < 2/3 D*pipe*. The downcomer is connected to the bottle through an eccentric conical expander either with the flat side up (as at Den Helder) or the flat side down (St.Fergus, Bintulu and Troll). Due to the expansion a further gas/liquid separation will take place. There is a slight preference for the flat-side-down orientation as no discontinuity in bottle slope takes place, which might disturb the development of stratified liquid flow (Figure 5).

### 3.3.2 Bottle section

This section encompasses (see Figure 3):

1. primary bottles
2. secondary bottles
3. equaliser system
4. liquid outlet header (or bottom header).

Gas liquid separation takes place in the first section of a primary bottle upstream of the first gas riser. Liquid is stored in the section farther downstream. Secondary bottles have a storage function for liquid only. The equaliser system is meant to equalise the pressure of the bottles.

### 3.3.2.1 Choice of primary and secondary bottles

The choice of the number of primary bottles (n$_{pb}$) and secondary bottles (n$_{sb}$) to be used in the multiple-pipe slug catcher depends on several factors:

1. Gas flow rate in the pipeline
2. Required liquid storage volume of the slug catcher
3. Plot size available (length available for bottles)
4. Diameter of the pipes to be used
5. Slope of the bottles
6. Choice between single or dual slope concept slug catchers.

It is important first to determine the number of primary bottles needed for efficient separation. In making this decision, allowance should also be made for possible future extensions and increase of flow rates through the unit. Therefore, although primary bottles are more costly to manufacture, the number of primary bottles should be generous but there should not be more than eight for flow distribution reasons.

The maximum flow rate a primary bottle can accept without liquid carry-over is a function of the physical properties of the gas and liquid, the bottle diameter and slope and the amount of liquid which can flow from the lower end of the primary bottle to other bottles.

For design purposes the worst case should be considered; i.e. no liquid flow to other bottles from the lower end. Also a certain degree of maldistribution of the slug over the bottles should be taken into account. It should be assumed that the most heavily loaded bottle receives 20% more than in the case of an even distribution (120/n$_{pb}$%). Furthermore if n$_{pb}$ > 1, n$_{pb}$ should be of an even number for symmetry reasons.

A recommended sequence of calculation to determine the numbers of primary and secondary bottles and their dimensions is given in (3.6). Definitions for maximum liquid volume capacities in slug catcher bottles are given in (Appendix 1).

### 3.3.2.2 Length of the entrance section of the primary bottles required for separation of droplets

The separation mechanisms in a slug catcher have already been described in (3.1.2). The first part of the primary bottle between the conical expander and the riser system should be long enough to achieve the required separation. The method of determining this length is described in (Appendix 2). It should be designed for a separation efficiency better than 99%. Gas flow velocities in the bottle should be no higher than 2 m/s to avoid that very long lengths will be required for separation.

### 3.3.2.3 Effect of bottle slope on choking

The bottles of the multiple-pipe slug catcher should slope downward. This will facilitate liquid filling by gravity and the flow of gas displaced by the incoming liquid to the gas outlet section. It is also required to avoid a slug catching effect: liquid stored in the primary bottle flows down as a stratified layer so as not to impede the ascending gas stream. Beyond a given liquid flow rate into the bottle (which is affected by the bottle slope), stratified flow can no longer be maintained and the bottle will become choked with liquid.

A model for the behaviour of choking due to liquid blockage in a bottle based on the Kelvin-Helmholtz criterion was created with the support of experimental simulation experiments and was subsequently used to predict the behaviour in two existing slug catchers with good agreements.

Figure 12 illustrates the predicted onset-of-choking for the Den Helder and St.Fergus slug catchers, as a function of the bottle slope, under inlet gas pressures of 70 and 110 bar, respectively. In the case of the Den Helder slug catcher the bottle slope (1.5%) is about the

optimal slope. Furthermore, the predicted onset flow (0.67 m³/s) is in good agreement with the 0.70 m³/s measured in practice. The slope of the St.Fergus slug catcher (0.4%), is well below the optimal value as predicted by the choking criterion (2.5%).

Based on the choking criterion 1% should be taken as a minimum value for the bottle slope in multiple-pipe slug catchers. Figure 12 suggests that from a choking point of view slopes up to 3% would be acceptable. However, large bottle slopes could lead to an impractical height of the slug catcher.

#### 3.3.2.4 The dual-slope approach

An attractive solution is the dual-slope concept. The advantage is that more efficient use is made of the liquid storage capacity of the bottles and excessive structural height is avoided. The first part of the primary bottles can be inclined at the angle optimal for filling rate and choke-free operation while the remaining sections of the primary bottles and the secondary bottles can be inclined at a smaller angle. Figure 13 shows the conceptual dual-slope design made for the Eemshaven slug catcher. The slope of the storage part of this unit is 0.4%. From a choking point of view this value is too low (see Figure 12) but still acceptable in this instance because this slug catcher was not intended to operate under fast flowing conditions. In general it is recommended to take a value of 1% as minimum slope for the secondary bottles and the storage part of the primary bottles. A slope of the separation section larger than say 2.5% may give only a minor improvement. Therefore a maximum value of 2.5% is recommended for the slope of the separation section. The most recent application of this approach can be found in the MLNG-2 slug catcher (Figure 5) and the Troll slug catcher (Figure 14).

### 3.3.3 Gas outlet section

This section consists of:

1. gas risers
2. gas outlet header(s)
3. gas outlet(s)

#### 3.3.3.1 Gas risers

Gas risers are primarily intended for the separated gas phase to leave the unit. They should be capable of preventing liquid carry-over when large volumes of liquid flow pass the base region of the gas risers, e.g. when a sphered slug arrives in the slug catcher. Although desirable, it is essential for them to function as liquid separators when flow velocity is high since efficient separation should already have taken place upstream of these parts (see 3.3.2.2). Also, excessively large gas riser diameters would otherwise be required.

The separation capability of a riser is determined by the load factor λ defined as:

$$\lambda = \frac{\rho_G}{\sqrt{\rho_L - \rho_G}} \cdot \sqrt{q}$$

λ ≤ 0.26 m/s should be taken so that droplets larger than 2 mm will settle out from the stream.

The condition when this criterion has to be met should be:

1. The risers are located at the primary bottle which receives (120/n₀₀)% share of the incoming slug (in the case of an even slug distribution over the bottles, the share would have been (100/n₀₀)%).
2. The slug is generated by sphering (or pigging).
3. There is no liquid flow from the heavily loaded bottle to the other bottles. This implies a maximum gas flow through the riser(s). If the number of risers per bottle is denoted by m, the gas velocity in the riser should obey the following relationships:

$$v_{SG} = \frac{\left(\frac{1.2}{n_{p0}}\right) Q_{pipeline}}{m \frac{\pi}{4} D_{riser}^2}$$

and

$$v_{SG\,5.0} = \frac{\sqrt{\Omega_{5.0}}}{n_{p0}}$$

where $v_{SG}$ is in m/s

At first sight, according to the equation it would appear that a very large riser diameter would be required if a superficial gas velocity ($v_{SG}$) value corresponding to the maximum pipeline throughput is assumed. It is advisable to assume this to correspond to the highest velocity used for pigging and sphering instead.

The riser should have a minimum height to allow liquid entrained in the riser gas stream to settle. The riser height should be at least 5 times its diameter or 5 m, whichever is less.

The possibility of a vertical gas/liquid junction, such as that in a T-piece, to cause separated droplets has already been mentioned in (3.1.2.5). In order to make use of this characteristic behaviour, it is necessary to have a second riser, located downstream of the first, to share between 25% and 30% of the gas flow. This approach was used for the MLNG-2 slug catcher (Figure 5). Reducers at the top of the risers control the split of flow through the first and second risers. The enhanced separation performance thus gained for this particular case will allow gas throughput to be increased by 100% without occurrence of carry-over. The advantage of this approach is that it will enable normal production through the terminal to continue uninterrupted even when one half of the slug catcher is isolated for maintenance. It is clear that sphering shall not be allowed during such a mode of operation.

There should not be more than two risers per bottle, especially if they are not sized to restrict and control the split of flow. Model tests have shown that downward and reverse flow in some risers can occur in such unnecessarily complicated systems.

### 3.3.3.2 Gas outlet header and gas outlet

The diameter of the gas outlet headers and gas outlets should not be made too small, because the pressure drop over the gas outlet system could become significant. The consequence of this is that after the slug has been received the liquid level in the bottles closest to the gas outlet will rise relative to the level in the other bottles (manometer effect) as has been observed with the model of the St.Fergus slug catcher.

Therefore the pressure distribution in the gas outlet risers should be balanced symmetrically as far as possible. This can be achieved by either by allowing gas to exit from both ends of the gas outlet header (see Figure 5 and Figure 15) or by placing diameter reducers at the top of each riser. (see Figure 5 and Figure 14).

### 3.3.3.3 Equaliser system

An equaliser header is used in the St. Fergus slug catcher (see Figure 3). Originally it was intended to equalise the distribution of liquid in the bottles. However, it was later found in model tests that the effect of an equaliser system on the slug catcher performance can be very sensitive to the slug catcher geometry and may not always be beneficial. In the model studies carried out on the St. Fergus slug catcher, it was found that the equaliser system had a negative effect on the performance. Gas flowing from the primary to the secondary bottles through the equaliser system caused liquid carry-over into the secondary bottles. Equaliser system should therefore not be used.

## 3.4 LIQUID OUTLET HEADER

Liquid outlet headers have commonly been designed with the same diameter as the bottles. The model studies carried out for the Eemshaven slug catcher (see Figure 13) showed, however, that a reduction in diameter (down to 75% of the bottle diameter) did not affect the slug catcher performance. It should not be reduced further due to the risk of blockage of the liquid outlet header by sludge or dirt which is always present in the lower part of the slug catcher. In relation to possible dirt accumulation it should be ensured that the header is accessible for cleaning. To prevent gas carry-under during liquid drainage of the slug catcher the liquid header should be below the lower end of the bottle.

### 3.4.1 **Liquid drainage**

Outlets from the liquid header should be positioned to ensure minimum accumulation of sludge in the manifold. At least two drains should be situated at low points of a manifold while liquid outlets (say three per manifold) should be spaced out evenly for the same reason and placed at 45 degrees from the vertical.

## 3.5 LIQUID LEVEL INDICATION AND CONTROL

Control of level in the slug catcher is essential for safe operation of a pipeline system. Level indication of a slug catcher can be influenced by several factors such as the presence of water and glycol, blockage due to sludge and accumulation of condensed liquid in impulse lines. As the density of water and glycol can be at least 30% greater than that of condensate, not only erroneous indications but also different liquid levels of combinations of condensate and glycol can exist in adjacent bottles. Therefore pressure tappings in the liquid outlet headers shall be placed appropriately so that no hindrance due to slugging can take place. An impulse line on the gas side of a pressure differential cell for level measurement is usually very long and traverses the total length of a slug catcher. It may be possible that liquid will condense inside this line. It should therefore be sloped in parallel with the bottles and sized generously, say 50 mm diameter, to allow for proper drainage.

### 3.5.1 Level indication by DP cells and liquid drainage

A typical arrangement used with good experience on the Hi-cal, Lo-cal and NOGAT slug catchers in Den Helder is shown in Figure 16. The gas side impulse line is mounted on the bottle and allows continuous drainage. A knockout pot for drainage is placed on this line just before reaching the DP cell. The high-pressure impulse line for the liquid side is connected to the DP cell 45 degrees away from the lowest point in the liquid outlet header where slugging is less likely to be present.

For integrity reasons, instrument bridles should not be used for slug catchers.

### 3.5.2 Effects of glycol

Erroneous effects due to glycol can be eliminated by a multi-DP cell combination applied on pressure tapping points at different and predetermined heights, provided the maximum level of glycol is known at the design stage. Nevertheless margins of uncertainty will still exist for some less important conditions.

### 3.5.3 Level indication by gamma densitometers

Although not yet generally applied, gamma densitometers should be considered for use in slug catchers which are expected to hold significant amounts of glycol. Several meters should be located along the length of a bottle. The presence of glycol will be identified immediately by the signal amplitude of a horizontally oriented meter.

## 3.6 RECOMMENDED SEQUENCE OF CALCULATION.

1. Determine (Vol*int*) by calculation (3.2).
2. Determine (Vol*buff*) according to process requirement of the system downstream.
3. Decide (D*bottle*) pipe diameter.
4. Decide (n*pb*) number of primary bottles (3.3.2.1).
5. Calculate distance from the end of the downcomer to the gas riser for separation (3.3.2.2).
6. Calculate the required storage length, L, of the bottle for storing the volume (Vol*SC*) and hence determine total length and width of slug catcher. If secondary bottles are to be used, L can be determined according to the available length of the plot for the slug catcher (Appendix 2).
7. Create sketch of the slug catcher showing its configuration and major dimensions. Evaluate and determine whether secondary bottles are required (Appendix 1). If the volume is less than the required Vol*SC*, either adjust the bottle length or the number of secondary bottles. Addition of secondary bottles will enable the overall length to become shorter. If adjustments have been decided, repeat sequence from step 4 and onwards.
8. A repeat volume calculation should be performed after all dimensions, including spacing between bottles, have been finalised.

## 4. MECHANICAL DESIGN

**4.1 GENERAL**

Slug catchers are an integral part of a pipeline system and shall meet the requirements of DEP 31.40.00.10-Gen. for category D fluid. The demarcation of the slug catcher with downstream facilities shall be indicated on the process engineering flow schemes.

**4.2 MAXIMUM ALLOWABLE OPERATING PRESSURE**

The MAOP of the slug catcher shall not be less than the MAOP of the feeding pipeline system if line packing is required for the operation of the pipeline system. If line packing is not required, then the MAOP of the slug catcher should still equal the MAOP of the feeding pipeline system as this will negate the requirement for separate overpressure protection. Alternatively, if line packing is not required the MAOP of the slug catcher may be lower than for the feeding pipeline system if a significant net lifecycle cost benefit can be demonstrated from lowering the MAOP and installing dedicated overpressure protection for the slug catcher.

NOTE: DEP 31.40.10.14-Gen. (and ASME/ANSI B31.8) allow incidental pressure up to 10% above MAOP. The MAOP can be as high as the design pressure.

**4.3 DESIGN FACTOR FOR HOOP STRESS**

The design factor to limit the hoop stress arising from pressure containment shall be selected according to DEP 31.40.00.10-Gen.

NOTE: The design factor applies to the nominal wall thickness.

**4.4 OTHER STRESS**

All loads shall be considered when determining combined stresses during pressure testing and operations. These loads will include:

- pressure;
- thermal expansion;
- passage of slugs or surges;
- foundation and support reaction;
- settlement;
- environmental loads.

Deformations due to the possible different settlements of the slug catcher and the connecting structures shall be accounted for.

For buried slug catchers, possible deformations predicted at the transitions between exposed and buried parts, due to different settlements of the slug catcher and the connecting structures, shall also be accounted for.

The total longitudinal stress due to the internal pressure and weight of catcher including content shall not exceed 2/3 of SMYS.

The equivalent stresses shall not exceed the limits specified in DEP 31.40.00.10-Gen.

**4.5 SUPPORTS AND ANCHORS**

ANSI/ASME B31.8, shall apply for the design of supports and anchors.

The foundation of locally supported slug catchers shall be in accordance with DEP 34.19.20.31-Gen.

The bottles of a buried slug catcher should be situated entirely below original ground level in areas with a natural slope similar to the downward slope necessary for the gravity fill of the bottles.

On a level plot, the bottles may be buried in a stable sand mound above the original ground level, with the liquid outlet header above the original ground level, or to reduce the height of the mound, in a shallow pit.

NOTE: Burial of a slug catcher in a sand mound is considered an effective means of protection against fire.

See Figure 17 for examples of burial design for slug catchers.

The visual impact of the slug catcher on the environment should also be considered when determining its level and requirements for burial.

## 4.6 MATERIAL SELECTION

### 4.6.1 Linepipe

**Amended per Circular 17/02**

Linepipe used for bottle sections of the slug catcher shall be in accordance with DEP 31.40.20.37-Gen.

### 4.6.2 Fittings

Fittings shall be in accordance with DEP 31.40.21.30-Gen.

### 4.6.3 Flanges

Flanges shall be specified on the basis of ASME B16.5 and/or MSS SP-44.

### 4.6.4 Valves

Valves shall be in accordance with API Spec 6D.

### 4.6.5 Prevention of brittle fracture

The selection of slug catcher materials exposed to low temperatures shall be in accordance with DEP 30.10.02.31-Gen.

A reference minimum metal temperature shall be established under the most adverse combination of depressurisation and climate. The lowest temperature occurring in the slug catcher during depressurisation shall be determined, taking into account the heat content of the slug catcher wall and the heat influx from outside.

Under certain circumstances the lower design temperature can be taken to be 50 °C above the reference minimum metal temperature. A detailed evaluation of the limiting values of primary local membrane stresses, accounting for the time-dependent relation between temperature and pressure during depressurisation, shall be performed to establish the applicability of the 50 °C relaxation.

## 4.7 WELDING

Welding shall be in accordance with DEP 61.40.20.30-Gen.

## 4.8 INTERNAL/EXTERNAL CORROSION PROTECTION

The potential for internal corrosion in the slug catcher shall be evaluated to determine the need for a corrosion allowance or other measures to mitigate internal corrosion.

Cathodic protection of a buried slug catcher shall be in accordance with DEP 30.10.73.31-Gen.

Anti-corrosion coating of both buried and non-buried slug catchers shall be in accordance with DEP 31.40.00.10-Gen.

4.9 OVERPRESSURE PROTECTION

Separate dedicated overpressure protection shall not be required if the MAOP of the slug catcher is not less than the MAOP of the feeding pipeline system.

If the MAOP of the slug catcher is less than the MAOP of the feeding pipeline system then it shall be safeguarded against overpressure by full flow relief protection in accordance with DEP 31.40.10.14-Gen.

4.10 MAINTENANCE

Ancillary equipment, such as PSVs, blowdown valves and liquid level shut down valves, which may require replacement shall be provided with the necessary isolation to permit maintenance without the shutdown and/or decommissioning of the slug catcher and other relevant facilities.

Both ends of headers shall be provided with end flanges for inspection access and for providing ventilation during the inspection. Both ends of liquid headers shall be provided with end flanges to facilitate the removal of sludge.

Requirements for the condition monitoring of buried slug catchers shall be established during the design stage and be designed to minimise the requirement for future excavation.

4.11 EMERGENCY DEPRESSURISATION

The requirements for emergency depressurisation shall be determined taking into account the potential exposure to fire.

Depressurisation of the slug catcher to a suitably low pressure shall be accomplished prior to any likely loss of containment due to the high temperature creep-induced failure of exposed vessel wall sections.

## 5. HAZARD AND RISK MANAGEMENT

### 5.1 OBJECTIVE

This section provides general hazard and risk management guidance for the layout and design of slug catchers.

It shall be demonstrated during the design stage that risks to personnel, loss of asset and production from hazards related to the slug catcher are tolerable and as low as is reasonably practical through its operational life.

Requirements for operations, incidents and emergency response should be clearly identified for inclusion in operating and maintenance manuals, emergency procedures etc.

### 5.2 HAZARD AND RISK MANAGEMENT ASSESSMENT

EP 95-0230 should be used as a framework reference for the application of hazard management tools and techniques.

HAZOP studies (EP 95-0313) of facilities should also cover the slug catcher and address the potential consequences of potential upstream and downstream causes for process deviation.

FIREPRAN (EP 95-0350) or an equivalent technique shall be used for the analysis of risks associated with hydrocarbon release and assessment of the effectiveness of possible design measures to reduce risk.

**Amended per Circular 61-03**

The FRED method or equivalent techniques shall be used to model leaks, fires and explosions.

All plausible causes of loss of containment, escalation and consequences shall be identified and analysed.

### 5.3 LOSS OF CONTAINMENT

Identification of potential leaks and causes of possible loss of containment should be addressed. These should include:

- overpressure;
- corrosion;
- external impact such as mechanical or fire/explosion from adjacent facilities;
- operational activities such as drainage and venting.

### 5.4 ESCALATION SCENARIOS

All factors which may lead to escalation in case of loss of containment, such as ignition and leak spread, should be addressed.

### 5.5 DESIGN CONSIDERATIONS

Possible design measures which may result in reduction of risk to personnel, loss of asset and production shall be identified and analysed on their effectiveness in reducing this risk.

The design measures which may be considered should comprise i.a.:

- location of slug catcher within a facility;
- overpressure protection;
- corrosion allowances;
- reduction of number of flanges and fittings;
- location and orientation of flanged connections to reduce heat loading (impingement and radiation) from escalating jet fires to slug catcher pipe and other facilities;
- (partial) burial of slug catcher;

- passive fire protection;
- isolation;
- segregated catchment and drainage systems;
- blowdown rate.

Sections of pipework and vessels subject to prolonged heat loading (e.g. due to jet or pool fires) may, under certain circumstances, rupture to cause a BLEVE (Boiling Liquid Expanding Vapour Explosion). The design shall ensure that the possibility of a BLEVE is negligible.

Visual impact should also be considered when determining the slug catcher level and requirements for burial.

## 6. REFERENCES

In this DEP reference is made to the following publications:

NOTE: Unless specifically designated by date, the latest edition of each publication shall be used, together with any amendments/supplements/revisions thereto.

**Amended per Circular 17/02**

### SHELL STANDARDS

Index to DEP publications and standard specifications — DEP 00.00.05.05-Gen.

Metallic materials - Prevention of brittle fracture — DEP 30.10.02.31-Gen.

Design of cathodic protection systems for onshore buried pipelines — DEP 30.10.73.31-Gen.

Pipeline engineering — DEP 31.40.00.10-Gen.

Pipeline overpressure protection — DEP 31.40.10.14-Gen.

Linepipe for critical service (amendments/supplements to ISO 3183-3) — DEP 31.40.20.37-Gen.

Pipeline fittings (Amendment/Supplements to MSS SP-75) — DEP 31.40.21.30-Gen.

Reinforced concrete foundations and structures — DEP 34.18.20.31-Gen.

Welding of pipelines and related facilities (Amendments/Supplements to ANSI/API Std 1104) — DEP 61.40.20.30-Gen.

EP HSE Manual: — EP 95-0000

Design — EP 95-0230

HAZOP — EP 95-0313

FIREPRAN — EP 95-0350

**Amended per Circular 61/03**

### AMERICAN STANDARDS

Gas Transmission and Distribution Piping Systems, 1989 Edition, plus Addenda B31.8a-1990, B31.8b-1990 and B31.8c-1992 — ASME B31.8

Specification for pipeline valves API Specification 6D — API 6D

*Issued by:*
*American Petroleum Institute*
*1101 L Street, Northwest*
*WASHINGTON, DC, 20037*
*USA.*

## 7. FIGURES

**FIGURE 1** VESSEL SLUG CATCHER WITH SEPARATE SURGE DRUMS

**FIGURE 2** NOGAT SLUG CATCHER AT DEN HELDER

**FIGURE 3** ST. FERGUS SLUG CATCHER

**FIGURE 4** GEOMETRY WGT SLUG CATCHER AT DEN HELDER

**FIGURE 5** MLNG-2 SLUG CATCHER AT BINTULU

**FIGURE 6** SLUG CATCHER FOR LEMAN COMPRESSION PLATFORM

**FIGURE 7** "PARKING LOOP" TYPE SLUG CATCHER FOR LOCATION AT A BOOSTER COMPRESSOR STATION

**FIGURE 8** PROBABILITY DISTRIBUTION OF DROPLETS AND THEIR DEPOSITION DUE TO TURBULENT DIFFUSION, GRAVITY AND CENTRIFUGAL FORCE WHEN ENTERING THE SLUG CATCHER

**FIGURE 9** EXPERIMENTAL RESULTS FOR SPLITTING RATIOS AT A BRANCH ARM 40 AND 60 DEGREES° DOWN (7.2)

**FIGURE 10** EFFECT OF A VERTICAL SIDE ARM ON GAS LIQUID SPLITTING

**FIGURE 11** CONSTRICTOR DESIGN

**FIGURE 12** THE ONSET-OF-CHOKING FOR A 36" OD BOTTLE AS A FUNCTION OF THE BOTTLE SLOPE

**FIGURE 13** CONCEPTUAL DESIGN OF EEMSHAVEN DUAL-SLOPE SLUG CATCHER

**FIGURE 14** BOTTLE GEOMETRY OF SLUG CATCHER FOR TROLL

**FIGURE 15** RECOMMENDED GAS OUTLET CONFIGURATIONS

**FIGURE 16** LEVEL INDICATION BY DP CELLS

**FIGURE 17** EXAMPLES OF BURIAL DESIGN

**FIGURE 1-1** THE FILLING DEGREE OF THE BOTTLES IN A MULTIPLE-PIPE SLUG CATCHER FILLED TO ITS MAXIMUM CAPACITY

**FIGURE 2-1** THE TIME REQUIRED TO SETTLE SMALL LIQUID DROPLETS AS A FUNCTION OF THE DROPLET DIAMETER IN THE FIRST PART OF A PRIMARY BOTTLE

**FIGURE 2-2** DROPLET SEPARATION EFFICIENCIES IN SLUG CATCHER BOTTLE (ρ₀ = 60 kg/m³, ρₗ = 600 kg/m³)

**FIGURE 2-3** DROPLET SEPARATION EFFICIENCIES IN SLUG CATCHER BOTTLE (ρ₀ = 40 kg/m³, ρₗ = 600 kg/m³)

**FIGURE 2-4** DROPLET SEPARATION EFFICIENCIES IN SLUG CATCHER BOTTLE (ρ₀ = 80 kg/m³, ρₗ = 600 kg/m³)

![FIGURE 1 VESSEL SLUG CATCHER WITH SEPARATE SURGE DRUMS](figures/16-cross-country-pipelines-and-offshore-03_p0024_fig01_figure-1-vessel-slug-catcher-separate-su.png)

**FIGURE 1    VESSEL SLUG CATCHER WITH SEPARATE SURGE DRUMS**

**PLAN**

The plan view shows the slug catcher (phase separator) consisting of multiple parallel horizontal vessel tubes arranged in a bundle. Labels visible:

- SLUG CATCHER (PHASE SEPARATOR) — label at top right of bundle
- GAS/LIQUID INLET — label at left, with arrow pointing to inlet manifold
- GAS OFFTAKE — label pointing to the gas offtake connection on the bundle
- Dimension: 24 m (overall length of tube bundle)
- Dimension: 2.8 m (overall width / tube spacing)
- SURGE DRUMS — label at far right, indicating the surge drum vessels

**ELEVATION**

The elevation view shows a side profile of the slug catcher vessel with associated piping and surge drum. Labels visible:

- SLUG CATCHER (PHASE SEPARATOR) — label at lower left
- GAS/LIQUID INLET 0.9 m — inlet nozzle, left side
- GAS OFFTAKE 0.75 m — gas offtake nozzle, upper left
- LIQUID DRAIN 0.6 m — drain nozzle
- GAS RETURN 0.4 m — gas return nozzle, upper right
- LIQUID OUTLET — label at lower right with arrow
- SURGE DRUMS — label at far right
- Dimension: 6.0 m (vessel diameter / height at inlet end)
- Dimension: 3.2 m (surge drum diameter)
- Dimension: 24 m (overall vessel length)

![FIGURE 2 NOGAT SLUG CATCHER AT DEN HELDER](figures/16-cross-country-pipelines-and-offshore-03_p0025_fig01_figure-2-nogat-slug-catcher-den-helder.png)

![FIGURE 3 ST. FERGUS SLUG CATCHER](figures/16-cross-country-pipelines-and-offshore-03_p0025_fig02_figure-3-st-fergus-slug-catcher.png)

![FIGURE 4 GEOMETRY WGT SLUG CATCHER AT DEN HELDER](figures/16-cross-country-pipelines-and-offshore-03_p0026_fig01_figure-4-geometry-wgt-slug-catcher-den-h.png)

![FIGURE 5 MLNG-2 SLUG CATCHER AT BINTULU](figures/16-cross-country-pipelines-and-offshore-03_p0026_fig02_figure-5-mlng-2-slug-catcher-bintulu.png)

1) Valves added to allow isolation of part of the slug catcher.
2) See (5.21) for details on expanders.

![FIGURE 6 SLUG CATCHER FOR LEMAN COMPRESSION PLATFORM](figures/16-cross-country-pipelines-and-offshore-03_p0027_fig01_figure-6-slug-catcher-leman-compression.png)

![FIGURE 7 "PARKING LOOP" TYPE SLUG CATCHER FOR LOCATION AT A BOOSTER COMPRESSOR STATION \(ONLY THE VALVES REQUIRED FOR OPERATION WHEN RECEIVING LIQUIDS ARE INDICATED\)](figures/16-cross-country-pipelines-and-offshore-03_p0027_fig02_figure-7-parking-loop-slug-catcher-boost.png)

![FIGURE 8 PROBABILITY DISTRIBUTION OF DROPLETS AND THEIR DEPOSITION DUE TO TURBULENT DIFFUSION, GRAVITY AND CENTRIFUGAL FORCE WHEN ENTERING THE SLUG CATCHER](figures/16-cross-country-pipelines-and-offshore-03_p0028_fig01_figure-8-probability-distribution-drople.png)

![FIGURE 9 EXPERIMENTAL RESULTS FOR SPLITTING RATIOS AT A BRANCH ARM 40 AND 60 DEGREES DOWN \(7.2\)](figures/16-cross-country-pipelines-and-offshore-03_p0029_fig01_figure-9-splitting-ratios-branch-arm-40.png)

**FIGURE 10    EFFECT OF A VERTICAL SIDE ARM ON GAS LIQUID SPLITTING**

Air/water experiment with pipe diameter of 0.038 m
and 0.025 m side arm.
(Vsg≃10 m/s and Vsl=0.056 m/s)

![FIGURE 10 EFFECT OF A VERTICAL SIDE ARM ON GAS LIQUID SPLITTING](figures/16-cross-country-pipelines-and-offshore-03_p0030_fig01_figure-10-effect-vertical-side-arm-gas-l.png)

* Vertically upward side arm

+ Vertically upward side arm
  bend at end of main pipe

![FIGURE 11 CONSTRICTOR DESIGN](figures/16-cross-country-pipelines-and-offshore-03_p0031_fig01_figure-11-constrictor-design.png)

**FIGURE 11    CONSTRICTOR DESIGN**

RECOMMENDED CONSTRUCTION

*(Diagram showing an inlet header (spherical vessel with liquid level) connected via an eccentric 'T' to an expander leading to multiple outlet pipes.)*

CENTRALLY LOCATED SPLITTER PLATE
(Not recommended)

Jetting of the condensate into the downcomer

*(Diagram showing inlet header with a centrally located splitter plate at 45°, with a downcomer indicated.)*

ECCENTRICALLY LOCATED SPLITTER PLATE
(Not recommended)

Guidance of the condensate along the downcomer wall

*(Diagram showing inlet header with an eccentrically located splitter plate, with a downcomer indicated.)*

![FIGURE 12 THE ONSET-OF-CHOKING FOR A 36" OD BOTTLE AS A FUNCTION OF THE BOTTLE SLOPE](figures/16-cross-country-pipelines-and-offshore-03_p0032_fig01_figure-12-onset-of-choking-36in-bottle-v.png)

![FIGURE 13 CONCEPTUAL DESIGN OF EEMSHAVEN DUAL-SLOPE SLUG CATCHER](figures/16-cross-country-pipelines-and-offshore-03_p0033_fig01_figure-13-eemshaven-dual-slope-slug-catc.png)

The isometric schematic shows a multi-bottle dual-slope slug catcher. Key labeled components include:

- FROM GAS LINE (24")
- INLET HEADER (24")
- DOWN COMERS (18")
- RISER HEADER (24")
- RISER (24")
- GAS OUTLET (24")
- BOTTLES (48")
- LIQUID OUTLET HEADER (48")
- LIQUID OUTLET

Overall dimensions shown: 15 m (width), 30 m (intermediate span), 256 m (total length).

Legend:
- BOTTLE PART AT 0.4% SLOPE
- BOTTLE PART AT 2.5% SLOPE
- BOTTLES 5, 6, 7, AND 8: PRIMARY BOTTLES
- BOTTLES 1, 2, 3, 4, 9, 10, 11, AND 12: SECONDARY BOTTLES

![FIGURE 14 BOTTLE GEOMETRY OF SLUG CATCHER FOR TROLL](figures/16-cross-country-pipelines-and-offshore-03_p0033_fig02_figure-14-troll-slug-catcher-bottle-geom.png)

The 2D side-elevation schematic shows the geometry of a single slug-catcher bottle. Key labeled components include:

- Inlet header: 36"
- 14"/24" expander
- Gas riser header: 48"
- Gas riser: 48"
- Separation section
- 3% slope
- 15% slope
- 48"/36" reducer
- 90° elbow
- 36" liquid outlet header

Dimensional annotations:
- 40°
- 45°
- 90°
- See note 1 (at inlet elbow region)
- See note 2 (at gas riser)
- L1 = 11 m
- L s = 103 m
- 5 m
- 176 m (total)

NOT TO SCALE

Notes:
1. 24" elbow followed by 24" × 48" eccentric expanders bottom flat.
2. Gas risers can be perpendicular to bottles giving an angle of 1.7° from vertical.

![FIGURE 15 RECOMMENDED GAS OUTLET CONFIGURATIONS](figures/16-cross-country-pipelines-and-offshore-03_p0034_fig01_figure-15-recommended-gas-outlet-configu.png)

![FIGURE 16 LEVEL INDICATION BY DP CELLS](figures/16-cross-country-pipelines-and-offshore-03_p0034_fig02_figure-16-level-indication-by-dp-cells.png)

![FIGURE 17 EXAMPLES OF BURIAL DESIGN](figures/16-cross-country-pipelines-and-offshore-03_p0035_fig01_figure-17-examples-of-burial-design.png)

## APPENDIX 1  LIQUID STORAGE CAPACITY OF A MULTIPLE-PIPE SLUG CATCHER

Figure 1-1 in this Appendix shows the liquid levels in the bottles for the liquid-full condition. The maximum liquid level mark in the primary bottle for both the single slope and the dual slope concept should be at the intersection of the centre line of the lowest gas riser (if there are two risers per bottle) with the lower inner wall surface of the bottle. For the dual slope concept in the same Figure, the gas riser was located at a distance of D₀/ tan θ₂ from the intersection of the two different slopes where θ₂ is the slope angle of the steeper bottle. Therefore, for the purpose of determining the maximum capacity of the slug catcher, assume that the volume in the partly filled part of the bottle, as depicted in Figure 1-1, is (x·B)·D₀·tanθ where it is the slope of the bottle under the riser. This is valid for both the single slope and the dual slope concepts.

The corresponding position of maximum liquid level in the secondary bottle will depend on the difference in slope and length between the primary and secondary bottles. The slug catcher and the lengths of bottles should be arranged so that the free surface of liquid in the secondary bottle when full should never be completely in the riser.

![FIGURE 1-1 THE FILLING DEGREE OF THE BOTTLES IN A MULTIPLE-PIPE SLUG CATCHER FILLED TO ITS MAXIMUM CAPACITY](figures/16-cross-country-pipelines-and-offshore-03_p0036_fig01_filling-degree-bottles-multiple-pipe-slu.png)

## APPENDIX 2    SEPARATION OF LIQUID DROPS IN A PRIMARY BOTTLE

The length of the primary bottle between its entry and (first) gas outlet riser is determined by the desired settling and separation efficiency. Two calculation approaches are shown in this Appendix. The first assumes a typical uniform droplet size for determining the settling time required. The second approach allows for variation of droplet size and makes use of a calculation model. The first is described mainly to present the basic equations for users to understand the relevant physical parameters of importance. In practice the second and more detailed approach, allowing for drop size variation, should be used whenever possible. Graphs have been provided as working tools to cover most typical situations.

### A.2.1    UNIFORM DROPLET SIZE APPROACH

If

$$Re = \frac{V_s \rho_G d}{\eta_G}$$

then, for Re < 1:

$$V_S = \frac{(\rho_L - \rho_G) g d^2}{18 \eta_G}$$

for 1 < Re < 10²:

$V_s$ follows from

$$C_W Re^2 = \frac{4}{3} \cdot \frac{d^3 \rho_G (\rho_L - \rho_G) g}{\eta_G^2}$$

for 10² < Re < 10⁵:

$$V_s = 1.76 \sqrt{\frac{(\rho_L - \rho_G) g d}{\rho_G}}$$

For the calculation of a droplet in a swarm, the relationship holds so that

$$(V_s)_{swarm} = Vs\ (1 - H)^n$$

where n ranges from 4.65 to 2.39 for 0.1 ≤ Re ≤ 500. Furthermore the conservative assumption is made that the droplet has to travel a distance D, so that

$$t_s = \frac{D}{(V_s)_{swarm}}$$

(Figure 2-1) of this Appendix shows for the Den Helder slug catcher settling time (t$_{settle}$) as a function of the droplet diameter for several values of H$_{liq}$. Rather arbitrarily it is assumed that droplets larger than 0.5 mm will settle. From (Figure 2-1) it is seen that this is achieved within about 4 seconds, even when the liquid hold-up fraction H is as high as 0.2.

## A.2.2 TURBULENT DEPOSITION MODEL FOR A NORMAL RANGE OF DROP SIZES.

In addition to the droplet settling behaviour described in the previous section, a deposition model refined to allow for additional and relevant factors has also been set up. It has been refined to calculate for an assumed droplet size distribution. It includes effects due to turbulence and allows for geometrical details of the 45-degree inclined downcomer, the primary bottle and the tee-junction to the gas exit riser.

Separation efficiency graphs in (Figure 2-2) through (Figure 2-4) of this Appendix are provided as work tools for determining the required primary bottle length for given expected gas flow velocities. The assumptions used for the calculation are listed below:

1 - Droplet size distribution is according to Katoaka with maximum values being 1000 and 750.
2 - Gas density 40, 60 and 80 kg/m³ corresponding approximately to 41, 62 and 83 bar pressure conditions (for standard natural gas).
3 - Liquid density 600 kg/m³.
4 - Liquid to gas volume ratio 0.05.
5 - Gas viscosity typically 0.000012 N.s/m².
6 - Downcomer is inclined at 45 degrees followed by a 1.5 D bend and an expander with flat side down.
7 - Downcomer to primary bottle diameter ratio is 2/3, i.e. typically 24 / 36.
8 - Gas riser to primary bottle diameter ratio is 2/3.

## A.2.3 PROCEDURE

Once the number of primary bottles and internal diameter of the material has been decided, one can proceed to determine the position of the first exit riser which is dependent on the desired slug catcher separation efficiency. Prior to selecting the appropriate graph from (Figure 2-2) through (Figure 2-4), it is essential to consider whether the intended configuration differs from that described. Of importance is to check whether the diameter relationships between the downcomer, primary bottle and riser are similar to that assumed mentioned above. If satisfactory, proceed to select the appropriate graph firstly according to gas density and followed by maximum assumed droplet size. The range of graphs has been provided also to assist users to determine sensitivity of certain parameters. For example, it can be seen that a higher gas density will tend to retard deposition and separation. Therefore, select a graph related to the higher gas density if one for the appropriate value is not available. Based on data collected from the slug catcher at Karratha in Australia operating with gas and condensate, it is recommended to assume 1000 μm as the maximum droplet size. For all types of design cases, it is appropriate to design for separation efficiencies of better than 95% and model is based on the assumption that liquid does not re-entrain once deposited. This may not be the case if the downcomer is vertical and excessive flow disturbance is expected. For those cases it is recommended to assume a smaller maximum droplet size of 750 μm instead.

Once the appropriate L/D value has been read off the graph, multiply by the internal diameter of the bottle to obtain the required settling distance before the riser. If the L/D value is larger than physically acceptable, the number and diameter of the primary bottles should be reconsidered.

![FIGURE 2-1 THE TIME REQUIRED TO SETTLE SMALL LIQUID DROPLETS AS A FUNCTION OF THE DROPLET DIAMETER IN THE FIRST PART OF A PRIMARY BOTTLE](figures/16-cross-country-pipelines-and-offshore-03_p0039_fig01_figure-2-1-time-settle-liquid-droplets-d.png)

![FIGURE 2-2 DROPLET SEPARATION EFFICIENCIES IN SLUG CATCHER BOTTLE \(ρ_G = 60 kg/m³, ρ_L = 600 kg/m³\)](figures/16-cross-country-pipelines-and-offshore-03_p0040_fig01_figure-2-2-droplet-separation-efficienci.png)

**FIGURE 2-2 DROPLET SEPARATION EFFICIENCIES IN SLUG CATCHER BOTTLE**
(ρ_G = 60 kg/m³, ρ_L = 600 kg/m³)

Two charts showing droplet separation efficiency curves for a slug catcher bottle, plotting L/D (y-axis, 0–30) versus V_gas in m/s (x-axis, 0–4), with efficiency contours at 80%, 90%, 93%, 96%, 99%, and 99.5%.

**Top chart:** D_max = 750 μm

**Bottom chart:** D_max = 1000 μm

![FIGURE 2-3 DROPLET SEPARATION EFFICIENCIES IN SLUG CATCHER BOTTLE \(ρ_G = 40 kg/m³, ρ_L = 600 kg/m³\)](figures/16-cross-country-pipelines-and-offshore-03_p0041_fig01_figure-2-3-droplet-separation-efficienci.png)

**FIGURE 2-3  DROPLET SEPARATION EFFICIENCIES IN SLUG CATCHER BOTTLE**
**(ρ_G = 40 kg/m³, ρ_L = 600 kg/m³)**

Two charts showing L/D (y-axis, 0–30) vs. V_gas (x-axis, 0–4 m/s) for separation efficiencies of 80%, 90%, 93%, 96%, 99%, and 99.5%.

**Upper chart:** D_max = 750 μm

**Lower chart:** D_max = 1000 μm

![FIGURE 2-4 DROPLET SEPARATION EFFICIENCIES IN SLUG CATCHER BOTTLE \(ρ_G = 80 kg/m³, ρ_L = 600 kg/m³\)](figures/16-cross-country-pipelines-and-offshore-03_p0042_fig01_figure-2-4-droplet-separation-efficienci.png)

**FIGURE 2-4   DROPLET SEPARATION EFFICIENCIES IN SLUG CATCHER BOTTLE**
**(ρ_G = 80 kg/m³, ρ_L = 600 kg/m³)**

*Top plot — D_max = 750 μm*

Chart showing L/D (y-axis, 0–30) vs V_gas (m/s) (x-axis, 0–4) for separation efficiencies of 80%, 90%, 93%, 96%, 99%, and 99.5%. Curves rise steeply from low gas velocities and flatten toward higher velocities. Higher efficiency curves lie above lower efficiency curves. D_max = 750 μm.

*Bottom plot — D_max = 1000 μm*

Chart showing L/D (y-axis, 0–30) vs V_gas (m/s) (x-axis, 0–4) for separation efficiencies of 80%, 90%, 93%, 96%, 99%, and 99.5%. Similar curve family to the top plot but shifted — at the same efficiency, lower L/D values are needed compared to the D_max = 750 μm case. D_max = 1000 μm.

*Last page of this DEP*
