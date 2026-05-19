# 300   Piping System Design

## Abstract

This section provides guidance in the design and installation of typical piping systems. It is intended for all users of this manual.

How to properly size piping systems is discussed, and good layout practices are illustrated. Methods of analyzing piping stresses and providing pipe stops and supports are reviewed. Design and support of small diameter piping are discussed. Considerations for design of buried piping are also given.

## Contents

| | Page |
| :--- | ---: |
| **310   Pipe and Valve Sizing** | **300-3** |
| 311   Economic Line Size | |
| 312   Selecting the Nominal Pipe Size | |
| 313   Line Sizing Considerations Other Than Economics | |
| 314   Items Needing Special Attention | |
| 315   Considerations for Various Flow Regimes | |
| 316   Economic Valve Sizing | |
| **320   Layout and Arrangement** | **300-22** |
| 321   Piping and Equipment Layout Development | |
| 322   Good Piping Practice | |
| 323   Manifolds | |
| 324   Pipeways | |
| 325   Rotating Equipment | |
| 326   Fired Heaters | |
| 327   Columns, Vessels and Heat Exchangers | |
| 328   Instrumentation | |
| **330   Flexibility, Restraint and Support** | **300-51** |
| 331   Piping Flexibility and Stress Analysis | |
| 332   Pipe Supports and Hangers | |

333    Pipe Restraints

**340    Small Diameter Piping    300-57**

341    General

342    Characteristics and Concerns

343    Pipe, Fittings and Connections

344    Thermal Relief Piping

**350    Buried Piping    300-61**

351    Problems Associated with Buried Piping

352    Corrosion Protection of Buried Piping

## 310 Pipe and Valve Sizing

In general, fluid flows through piping one of two ways: 1) energy must be added to move the fluid or 2) the available pressure drop is adequate for fluid flow. In the latter, the proper line size is the smallest one that passes the required flow without exceeding practical velocity limits. When energy must be added, the proper line size is the one resulting in the lowest combined investment and operating cost over the payout period of the plant. As this is the more common of the two cases, it will be discussed first.

## 311 Economic Line Size

As noted in Section 100, piping is one of the largest single cost items in nearly all process plants. Because of its significant cost, piping should be of an economical size and/or adequate to meet operational requirements. Fortunately, piping is available in relatively few sizes so the problem of finding the economic size is greatly simplified and a detailed study of each pipe line in a process plant is generally not justified. However, many off-plot lines should be studied in detail because of the long lengths and large capital investment involved.

It is important to note that **economic line sizing can only be applied to pumped fluids or compressed gases.** Economic line size is a balance between the installed cost per unit length of pipe and the cost to provide the necessary energy to move the fluid (the incremental investment cost of pump or compressor and the cost of power). The economic line size is independent of length of line, control valves, or any other superimposed pressure drop not affected by a change in line size.

It is of little economic value to evaluate in great detail the precise size of a line since 1) pipe is available only in certain nominal sizes and 2) the economic relationship between installed costs and energy is to the 1/6 power and therefore only needs to be approximate. Thus, the bulk of lines in a process plant can be sized rapidly by rough correlations with a minimum chance of significant error.

For most liquids pumped in process plants where the viscosity is in the range of 1 to 10 cs, the economic velocity ranges from 10 to 12 fps for on-plot lines NPS 6 and larger and 6-8 fps for off-plot lines. The economic velocity for compressed gases is approximately 40 times the cube root of the specific volume in cubic feet per lb mass for on-plot lines and 25 times the cube root of the specific volume for off-plot lines.

However, a practical limit to the pressure drop in pumped or compressed process lines exists. High pressure drops will require the use of higher pressure pumps and may increase the design pressure of vessels and other equipment. High pressure drops may also increase the chances of design error, since the accuracy required in calculating losses through pipe and fittings is increased. Therefore, the following limits per 1000 feet of pipe are suggested:

| Liquids            | 25 to 30 psi |
| --- | --- |
| Gases              | 10 to 15 psi |
| 150-psig steam     | 4 or 5 psi   |
| Low pressure steam | 1 or 2 psi   |

Under special conditions and for short lines, higher pressure drops than the recommended limits given can be tolerated. An example of this would be a very short pipe fixed between two vessels.

It is the responsibility of the engineer to assure that his project economic conditions do not alter the line size selected. However, it should be noted that wide variations in costs result in very little change to the economic diameter. This is because the economic diameter is inversely proportional to the 1/6th power of the ratio rF/KS. For example, doubling the installed cost of piping (such as using stainless steel piping) results in only an 11% decrease in economic diameter. This is generally not enough of a change to alter the nominal pipe size selected. **Therefore, unless unusual project economics exist, it should not be necessary to correct the economic velocity.** If those conditions do occur, Figures 300-1 and 300-2 have been provided as a quick method to correct the suggested economic velocity provided above (10-12 fps for on-plot lines) using actual project cost data. Otherwise, a more rigorous calculation may be performed using the following method.

![Fig. 300-1 Economic Velocity Correction Factor for Gases](figures/01-overall-piping-design-standards-10_p0004_fig01_fig-300-1-economic-velocity-correction-f.png)

![Fig. 300-2 Economic Velocity Correction Factor for Gases](figures/01-overall-piping-design-standards-10_p0005_fig01_fig-300-2-economic-velocity-correction-f.png)

The total annual comparable cost of piping can be expressed as

$$C = \frac{FD}{r} + 7.85 \times 10^{-6} \frac{KSQ^3 f}{D^5}$$

(Eq. 300-1)

where:

$$F = (1 + X) L$$

$$K = \frac{Yk}{r} + 8760 \text{ ct}$$

(Eq. 300-2)

- C = Amortization of investment cost and annual operating cost
- c = Power costs converted to dollars per hydraulic horsepower
- D = Internal pipe diameter, in.
- EDMI = Engineering Department Materials Index

- F = Total installed piping costs, $/dia.in./ft (including painting, steam tracing, and insulation)
- f = Friction factor (see *Fluid Flow Manual*)
- K = Annual cost per hydraulic horsepower for pumps or compressor (including both amortized investment and operating costs), $/hp
- k = Purchased machinery cost per hydraulic horsepower

$$k = 255 \frac{\text{Current EDMI}}{720} \text{ for centrifugal pumps}$$

$$k = 495 \frac{\text{Current EDMI}}{720} \text{ for compressors}$$

(Eq. 300-3)

- L = Group II costs of installed piping, dollars per diameter inch per foot of pipe (Group II costs are material costs plus direct field expenses)
- Q = Flow rate, gpm
- r = Payout period (before taxes), years
- S = Specific gravity (water at 60°F = 1.0)
- T = Temperature, °F
- t = Load factor,⁴/100 of the year the machinery will operate
- X = Group 1B costs as a fraction (⁴/100) of Group II costs (Group 1B costs are indirect field expenses)
- Y = Multiplier applied to machinery purchase cost to account for installation of complete unit (includes foundation, piping manifold, auxiliary piping, power distribution, Group II and Group 1B costs)

## 312 Selecting the Nominal Pipe Size

The economic diameter most often will be somewhere in between two nominal pipe sizes. Economically, it is generally not worthwhile to make a complete analysis on which size is to be selected. When selecting the smaller size line, initial capital investment for piping is smaller and the investment operating costs of pump or compressing the fluid is larger. Conversely, selecting the larger size line yields greater initial capital investment with a resulting lower operating cost. However, **for either line size selected, the total yearly cost over the payout period will be nearly the same**. From the standpoint of economics, it doesn't matter which is selected. However, from an engineering standpoint, selecting the larger pipe would contain more design flexibility and conservatism allowing for any late design

changes or corrections. The added advantage of lower operating costs may also suggest selecting the larger size pipe. On the other hand, this is an opportunity to reduce investment costs. Engineering judgement should be used in selecting nominal pipe size. Some problems to consider are:

- Does going to a smaller line size result in pressure drops in excess of those allowed above?
- Does going to a smaller size pipe result in an erosion problem for fluids such as DEA? Consult a materials engineer if there is concern.
- Does added pressure drop in the system caused by going to a smaller size pipe result in increasing the rating of the piping system (i.e., from ANSI Class 150 to Class 300) or increase the design pressure of columns, vessels, and heat exchangers in the system?
- If the line is steam traced, does going to a smaller line result in fewer tracers?
- Is there an excessive surge pressure problem caused by quick closing valves shutting off against too high a velocity? See Section 600 and the *Fluid Flow Manual*.
- Special consideration should be given to gas velocity. High gas velocities cause noise problems, so velocity should generally be limited to about 100 (V)$^{0.5}$ ft/sec, where V is the specific volume in ft$^3$/lb$_m$. However, for most conditions, this limit will not be reached.
- It should be noted that, for low flow rates (gpm) the economic line sizing calculations will indicate undersized lines. That is, the diameters suggested result in pressure drops which are higher than the suggested limit of 30 psi per 1000 ft for liquids and 15 psi per 1000 ft for gases. As a result, for low flow rates, most process lines should be sized to meet the highest allowable pressure drop. **In any circumstance, the pressure drop should always be checked in the** *Fluid Flow Manual* to see that it is under the allowable limit.

## 313 Line Sizing Considerations Other Than Economics

If lines have been sized by economics, it will still be necessary to "design" the line to determine the hydraulics of the system, i.e., calculate pressure drops, determine valve sizes, establish required pump heads, establish compressor pressure, etc.

If the line is one where considerations other than simple economics, or where NPSH, cavitation, erosion, change of state, etc., affect the selection of line size, the following general procedure for analyzing a piping system may be found helpful.

The first step should be an examination of the individual pipe system involved and, if useful, preparation of a simple system sketch with attention focused (under both normal conditions and extreme conditions) on:

- Flow rate
- Fluid state (liquid, vapor, mixed-phase)

- Terminal conditions and their effect on line sizing
- Energy sources (pumped, compressed, gravity)
- Pressure drop in equipment and control devices in the system (exchangers, furnaces, control valves, orifices, strainers, etc.)
- Continuous or intermittent flow. (Smaller pipe is frequently warranted in cases of intermittent flow.)
- Fluid density
- Viscosity

In examining the individual system, the engineer may not need to establish all of the above factors precisely before proceeding with line sizing. However, effective prosecution of design work demands that the engineer proceed on the basis of sound judgment along the following lines:

## Determine Flow Quantity

**Nominal Flow Rate.** This rate is shown on the process flow diagram on an operating-day basis and should be used for economic sizing of most process lines.

**Maximum Flow Rate.** The maximum design flow rate provides for the variations needed for good process control. Do not use the maximum design flow rate for economic line size calculations. Allowances beyond the nominal flow rate should, however, be provided in specifying the conditions to be met by the primer mover (pump or compressor) and by the control valve.

**Alternate Operating Conditions.** Startup, shutdown, and pump-out situations may conceivably be governing conditions for the flow rate employed in sizing certain lines. It is suggested, however, that the engineer first size the line on the basis of normal nominal flow rate and then consider the above items for the lines involved. Experience has shown that such factors will only infrequently influence the line size selected. Usually they are accommodated by appropriate specifications for the prime mover and control valve.

**Allowances for Future Capacity Increase.** Such allowances should only be added to the nominal flow rate if specifically spelled out in the design basis for the plant. This is management's responsibility and it is not the prerogative of the design engineer to provide such extra capacity when sizing process plant lines. When the economic size falls between two nominal pipe sizes, future capacity considerations may justify using the larger size.

## Determine Fluid State

The fluid state should be defined and treated accordingly in pressure drop calculations. Determine whether the fluid is:

- Normal liquid or vapor
- Flashing flow (2-phase liquid-gas)
- Slurry (2-phase solid-liquid)

## Determine Terminal Conditions

Determine conditions at the upstream and downstream ends of the piping system. The datum for pressure and level in an operating container, whether used for pumped liquid, gravity flow, or pressure letdown is selected from Figure 300-3.

> **Table - Fig. 300-3 Pipe Terminal Conditions, Container at Upstream/Downstream End of Line** - see [source crop](tables/01-overall-piping-design-standards-10_p0009_tbl01_fig-300-3-pipe-terminal-conditions.png)

**Fig. 300-3** Pipe Terminal Conditions, Container at Upstream/Downstream End of Line

| **Container** | **Upstream (Suction)** | **Downstream (Discharge)** |
| :--- | :--- | :--- |
| **Pressure:** | | |
| Equipment or Utility Supply Headers | Minimum operating pressure | Maximum operating pressure consistent with the suction<sup>(1)</sup> |
| **Fluid Levels:** | | |
| Tank | Bottom of operating range (usually 2 ft above tank bottom) | Full |
| Horizontal Vessel | Bottom gage nozzle or 0.1 diameter above bottom | Full (or to highest<sup>(2)</sup> point in the system) |
| Vertical Vessel | Bottom head-to-shell seam | Full (or to highest<sup>(2)</sup> point in the system) |
| Column | Bottoms: Bottom head-to-shell seam<sup>(3)</sup> Side draw: Outlet nozzle | Feed or reflux nozzle elevations |

(1) In circulating systems such as column reflux, the upstream and downstream static pressure are obviously related.

(2) In some cases, the minimum and maximum operating levels may differ from these. Consider the circumstances and apply your engineering judgment to each.

(3) Assume 10 ft above grade for preliminary calculation when suction lines are overhead.

The importance of accurate definition of these data will depend upon the effect of variations in them on the capacity of the system. High accuracy is usually important only for pump section with boiling liquids, or high static pressures or elevations compared with system friction losses.

## Determine Energy Sources—Process Pressure, Gravity, Pump or Compressor

In many cases where a line passes from a process vessel at relatively high pressure to one at a lower pressure, small lines can be used, since the pressure available has to be dissipated any way. It is, of course, important to consume the right relative proportions in the line and in a control valve so that satisfactory control is achieved.

Selecting line and valve sizes for lines between two points with fixed pressures is not based on economics (as no pump or compressor is involved) but can be done on a trial and error basis. Assume a size and check the total pressure drop. If it is not close to the AP available, try the next size larger (or smaller as appropriate). There can be some trade-off between line and valve size, however. For example, it may cost less to install a 14-inch line with 10-inch valves than a 12-inch line with 12-inch valves, while both have the same overall pressure drop. Generally, however, it is most practical to determine the smallest line size (with same size valves) that has less total line loss than is available, then check to see if using one size smaller

valves still gives total line loss less than is available. For more information on economic valve sizing, see Section 316.

Frequently, where gravity is the source of energy, lines larger than normally economical may be required. In some instances, particularly where lines are long, it may be most economical to install a pump and then employ the smaller piping this makes possible. Where pumps and compressors are the energy source, economic line sizing, followed by pressure drop calculations to assure that proper pressure is supplied by the machine, is required.

#### Determine Dynamic Losses—Pressure Drop in Equipment and Control Devices

In addition to the pressure drop through the piping, dynamic losses will normally include one or more of the following elements:

**Control Valve.** There is no set value for control valve allowance. For the normal pumped liquid system, controlled through a range of 50 to 115% of nominal flow rates, control valve allowance will usually be around 50% of the total dynamic head loss at the **nominal** flow rate. It should be at least equivalent to the pressure drop through a control valve (globe pattern) one size smaller than the line with valve wide open at **maximum** flow.

**Heat Exchangers.** Realistic maximum pressure drops specified on the design data sheets should be used. These may vary over a wide range, depending on stock properties and exchanger arrangement. For water and light hydrocarbon through exchanger tubes, pressure drop is usually about 5 to 10 psi. However, it can be considerably higher.

**Strainers.** These are normally sized for a pressure drop of 1 to 5 psi.

**Flow Meter Orifices or Flow Nozzles.** Pressure drop can be figured as ½ of the meter differential at nominal flow rate because the orifice will usually be sized for nominal flow at 70% of full scale. The usual meter ranges are 100 inches of water for liquid lines, 50 inches of water for low pressure gas and steam lines, and a minimum of 20 inches. Thus, appropriate drops would be about 2 psi for liquids and 1 psi for gases. On very large lines, actual meter design and static pressure recovery should be considered.

## 314 Items Needing Special Attention

### Vapor Traps in Liquid Lines

Vapor traps in liquid lines, particularly in low velocity pump suction lines, must be avoided. Many horizontal suction pumps require a reducer at the pump flange. Use an eccentric reducer with the flat side up, and install a drain valve at the low point for plant cleanup. If the suction line comes from above the pump, a reducing elbow may be used in a vertical plane without a drain valve. Where high spots in the line cannot be designed out, install a vent with a bleeder valve for evacuating the vapor.

## Liquid Traps

Liquid traps, pockets, and dead ends should be avoided in all piping, particularly lines conveying water, caustic acid, materials which may congeal or freeze, fluids which may form a corrosive condensate, and fluids containing solids which may settle out. Where low spots and dead ends cannot be avoided, install a drain valve for system cleanup.

To "knockout" liquids in a vapor line, one option is to create a "wide spot in the line." A Knockout (K-O) pot or slug-catcher may be used for this purpose. (A knockout pot usually refers to a vessel in a processing facility; a slug-catcher usually refers to a knockout pot in a pipeline or production gathering system.)

## Water Hammer

When a valve is suddenly closed against a flow, a very heavy knocking sound may be heard as the entire pipe vibrates. The inertia of the flowing fluid increases the pressure at the valve (surge pressure) and the pressure wave propagates along the pipe, sometimes with enough force to fracture the pipe. This phenomenon is called water hammer, although any fluid may cause this effect. Refer to the *Fluid Flow Manual*, Section 800 for more information about how to calculate surge pressure.

Water hammer may be prevented by using a slow-action control valve. Where a quick-closing valve is necessary, many of the problems associated with water hammer may be circumvented by the use of a surge drum. A surge drum upstream of the control valve will slow down the acceleration and deceleration of the fluid in a piping system subject to constant sudden opening and closing of a control valve.

## Pump Suction

Always check NPSH available at the pump unless it is obviously adequate (short lines, large submergence with liquids sub-cooled more than 100°F below their boiling point). Always check NPSH at least 10% above maximum flow. Required NPSH increases and available NPSH decreases, both varying about as the square of the flow rate. **An inadequate suction line can very effectively choke the capacity of an entire plant.** Refer to Section 200 of the *Pump Manual*.

When NPSH is not governing, pump suction lines should be the same size as for the discharge line. When NPSH is governing, suction lines will usually be one size larger, perhaps two. This is particularly true of liquids being pump at or near their boiling point such as:

- Column bottoms, reboiler, and reflux
- LPG or other light products stored at their bubble point
- Boiler feedwater from deaerator or steam condensate from a condenser or flash drum

## Critical NPSH Suction Lines

With saturated liquids, NPSH at the pump is independent of the pressure above the liquid in the suction vessel. Thus, the vessel is typically elevated to provide the required NPSH.

An economic installation then is a balance between the investment in suction vessel elevation, line size and type of pump used. Minimizing dynamic loss by increasing line size is probably the most effective first step. However, don't overlook low NPSH centrifugal pumps (low speed horizontal, or vertical "can-type" units) before increasing elevation of the suction vessel. (See the *Pump Manual*.)

## Vapor Pressure

Within any line designed for liquid flow, the pressure should not be permitted to fall to the bubble (boiling) point at any locations. Generally, larger fittings or lines are required. Examples of where this may occur are:

- Column side draws. Loss in entrance (nozzle) and elbow may exceed liquid head in draw-off pan. It may be necessary to increase nozzle and elbow one size and then reduce to line size.
- Meter runs—through upstream fittings and below orifice
- A throttling valve—outlet
- Syphons—any point upstream
- Reciprocating pumps with long suction lines—pulsating pressure may fall below bubble point
- Pump suction (NPSH)—(see foregoing discussion)

## Hydraulic Surge

Line sizes for liquids are sometimes influenced by hydraulic surges which occur when the flow is rapidly decelerated, such as in loading lines to trucks and airplanes. The magnitude of such pressure surges is normally inversely proportional to the flow area, so that they can be substantially reduced by use of larger lines. See Section 800 of the *Fluid Flow Manual* for methods to calculate surge pressure.

## Minimum Velocities

Velocity may have to be kept above a certain minimum to keep solids in suspension, keep the line clean, or to minimize temperature drop in a hot line or temperature rise in a cold line, etc.

## Pumps with Two or More Services

Pumps frequently discharge to two or more destinations at different flows and different pressure levels, such as column reflux and overhead product to storage. Only one of these discharge cases, the one governing pump head, will normally be an economic line size case. In the other case, the line should be only large enough to provide capacity for maximum demand and control allowance between the established static pressure levels.

## Pressure Letdown

Substantial pressure reduction often occurs within a process plant, on products leaving the plant to store, on boiler blowdown, and on condensate letdown to flash drums. As with branched lines mentioned above, they need to be only large enough for maximum capacity and to provide for control. But there are some other things to watch out for:

**Flashing.** When not on the discharge of a pump, the liquid may be at or near its boiling point and start vaporizing upstream, downstream, or within the control valves. In high pressure systems, it is usually best to avoid flashing in the valve piping. The control valve would then be sized for saturated liquid inlet and downstream piping sized for flashing flow.

**Cavitation Through Control Valves.** A control valve produces a pressure drop by reducing the area between the seat and the plug (disk or ball in rotary valves). Process fluid accelerates through the reduced opening. As the fluid accelerates, pressure in the area of acceleration drops, then recovers partially as the fluid enters the valve/piping cavity and decelerates (Bernoulli's equation).

If the pressure in the area of acceleration drops below the vapor pressure of the process fluid, the process fluid will flash and form vapor bubbles. If the pressure recovers above the vapor pressure of the fluid, the vapor bubbles will collapse (implode) and go back into solution. The implosion of the bubbles generates so much energy that metal is physically washed away from the valve body and the downstream piping. Cavitation is accompanied by noise that can be described as "a cement truck with its rotating drum full of gravel," only louder. Severe cavitation can generate noise in excess of 110 dBA.

Cavitation can be treated by selecting a valve with a lower pressure recovery coefficient, e.g., a valve where the process fluid is impinged upon itself from opposite sides of a cage (anti-cavitation cage trim) or by taking the pressure drop in several stages. Refer to the *Instrumentation and Control Manual*, Section 970 "Control Valve Problems" for additional information.

**Erosion.** Very high velocities (above 100 to 200 ft/sec) **in flashing liquid** lines can result in erosion of piping if the liquid bombardment destroys or prevents protective coating of corrosion products. As this is dependent on pipe material and the degree of corrosion, consultation with the materials engineer is desirable for such cases. For flashing condensate in carbon steel lines, a limiting momentum has been suggested to minimize erosion at elbows, tees, etc. This is expressed as a maximum reaction force on the fitting (V²/2gY) of 300 lbf/ft² of pipe cross-section area. Erosion can be minimized by using long sweep (5-diameter) bends, or more erosion resistant material. t generally is not a problem except with pure compounds or narrow boiling point mixtures.

### Vortices

A vortex is a whirling liquid moving in concentric circles around a vacuum or cavity in the center of the circle. Vortices occur most frequently on bottom outlets of vessels and columns and can inhibit flow.

A vortex breaker is usually nothing more than a small plate welded above an outlet which disrupts the circular pattern of a forming vortex. A vortex breaker per Standard Drawing GE-C99913 (see the *Pressure Vessel Manual*) should be provided on the bottom outlet nozzle from each vessel where two phases may be present and/or which provides flow to a pump suction.

## Gravity Flow

When there is no pressure difference other than level to cause flow, check the line elevation and pressure gradient at design flow to be sure the upstream level is adequate. The line can usually be made smaller by first dropping through a vertical leg followed by a horizontal line running full, rather than by providing a nearly horizontal run flowing only partly full.

## Meter Runs

Occasionally meter runs must be larger than economic lines to provide proper flow element to line diameter ratio. They should be considered when sizing lines in consultation with the instrument engineer.

## Headers

When headers are used to distribute flow to a number of similar parallel units, such as heat exchangers, it will usually be cheaper to make the header pressure drop low to avoid the need for individual control on each of the parallel paths. The header pressure drop should be consistent with the tolerable variation in flow.

## Flow Imbalance in Parallel Piping Systems

Flow imbalance to multiple furnace passes can result in coke deposition on furnace tubes; flow imbalance to parallel heat exchangers can result in hot spots on tubes or process upsets. Equalizing the pressure drop in the parallel piping will balance the flow.

When mixed-phase flow must be distributed to parallel passes of a furnace or to parallel identical heat exchangers, the piping should be symmetrical to prevent the separation of phases and should run in a plane of symmetry for at least ten diameters before each point at which it splits. Each pass to the furnace also usually includes a balance valve for manual or automatic flow control. The furnace outlet must be hydraulically balanced, but piping symmetry is not required.

Refer to the *Fired Heater and Waste Heat Recovery Manual*, Section 400, for more information on furnace piping design.

## Furnace Transfer Lines

Design of transfer lines from a furnace to a column should always be coordinated with the furnace design as the pressure drop affects outlet pressure and performance of the furnace. Vacuum column transfer lines are particularly critical. Considerable savings can be realized by using the minimum adequate size, particularly with alloy lines. Refer to the *Fired Heater and Waste Heat Recovery Manual*.

#### Column Overhead Lines

Large column overhead lines warrant special consideration. With pressure fixed at the top of the column by process conditions, pressure drop in the overhead line may affect:

- Condensing pressure and temperature (or at least the allowable pressure drop through the condenser)
- Condenser size and cost
- Cooling water required
- Vacuum system size and steam requirements in the case of a vacuum column
- Piping flexibility. Too large or too heavy a line may make it difficult and expensive to provide adequate flexibility

#### Vertical Thermosiphon Reboiler Nozzles

In thermosiphon reboilers, the only head available for flow is the difference in density between the liquid in the column bottom and the vapor-liquid mixture in the reboiler. Piping is kept as short as possible and friction losses in the piping must be kept below a reasonable maximum so that it is not a significant part of the available head for circulation. For vertical thermosiphon reboilers, the following simple rule of thumb relating diameter only to the reboiler duty has given good results:

Reboiler Inlet: $D^2/q = 12$ to $15$

Reboiler Outlet: $D^2/q = 25$ to $30$

where:

D = Inside diameter, in.

q = Duty, MMBtu/hr

## 315 Considerations for Various Flow Regimes

#### Two-phase Flow

Refer to the *Fluid Flow Manual* for procedures on determining line size and pressure drops for piping systems operating in two-phase flow.

#### Flashing Water

As may be expected, flashing water lines (such as condensate return lines) have capacities far less than a water line that is not flashing. Calculations have shown that the capacity of a flashing water line with line pressures up to 1000 psig at the inlet and atmospheric pressure at the outlet is about 35% of the capacity of the line if it was not flashing.

See Section 350 of the *Utilities Manual* for further discussion of flashing water line sizing. In addition, the program PIPEFLOW-2 can perform flashing calculations.

## Gas Flow in Short Pipelines

Accurate calculation of the pressure loss-flow relation for short gas lines normally requires the use of complicated flow formulas in order to correct for the effect of kinetic energy change on the pressure loss.

The flow calculations for short lines can be simplified somewhat if one assumes isothermal flow (PV = constant) but are quite tedious if one tries to compute the exact pressure drop with proper allowance for temperature drop along the line.

Figure 300-4 can be used to determine the pressure drop for gas flow in short pipelines.

**Fig. 300-4** Pressure Drop for Gas Flow in Short Lines

![Fig. 300-4 Pressure Drop for Gas Flow in Short Lines](figures/01-overall-piping-design-standards-10_p0016_fig01_fig-300-4-pressure-drop-gas-flow-short-l.png)

The critical pressure ratio for k = 1.4 is:

$$\frac{P_{c1}}{P_1} = \left(\frac{2}{k \cdot (k+1)}\right)^{1/2} \cdot \frac{G}{P_1} \left(\frac{P_1 \cdot V_1}{g}\right)^{1/2}$$

(Eq. 300-4)

The critical pressure ratio for isothermal flow (k = 1.0) is:

$$\frac{P_{cr}}{P_1} = \frac{G}{P_1} \left( \frac{P_1 \cdot V_1}{g} \right)^{1/2}$$

(Eq. 300-5)

where:

- G = mass flow, lb/sec-ft²
- P_cr = critical pipe outlet pressure, lb/ft²
- P_1 = inlet pressure, lb/ft²
- P_2 = outlet pressure, lb/ft²
- V_1 = specific volume of gas at inlet, ft³/lb
- f = friction factor
- g = 32.2
- k = ratio of specific heats for gas
- L = pipe length, ft
- D = inside pipe diameter, ft

The specific heat ratio, k, is 1.4 for air and diatomic gases such as oxygen, nitrogen and hydrogen and between 1.0 and 1.4 for more complex gases. Whether it is 1.0 or 1.4 generally causes only minor differences in the pressure drop calculation.

## Flow of Expansible Fluid

When expansible fluids flow through piping systems with varying diameters (such as may exist in gas transmission lines), the following conclusions appear to be true:

The order in which the fluid resistances (i.e., pipe diameters) are arranged has no effect on the total pressure drop of the system provided the pressure loss caused by the change of kinetic energy is not large compared to the friction loss. This is true regardless of the density-pressure relation for the expansible fluid. (Designers of gas transmission lines have long been aware that this is true for a gas for which density is proportional to pressure.)

The order in which the fluid resistances are arranged does have some effect if the ratios of length to diameter are small. For such conditions it appears that, if pipes of several diameters are to be used, maximum capacity is secured by installation of the small pipe at the upstream end of the system.

Detailed calculations (see the *Fluid Flow Manual*) should be made to assure the correct design.

## Slugging in Vertical Lines

Gas-liquid mixtures flowing in a vertical line with too low mixture velocities may experience slugging. This occurs when the liquid velocity in the mixture is not sufficient for it to be swept along with the gas. The liquid "holds up" in the line until sufficient pressure is built up to push the slug through the line. Increasing the velocity of the mixture by decreasing the line size will prevent slugging from occurring. Pressure drops of up to 70 psi per 1000 ft are generally required for mixtures of low density flowing upwards in vertical lines.

## 316 Economic Valve Sizing

Block valves are used extensively in all process piping systems. Because of the high cost of quality valves, they should be economically sized to minimize capital investment without appreciably increasing operating cost. The economic valve size may change for each project. It is therefore recommended that the economic valve size criteria be determined for each project using current costs.

For manufacturing facilities, however, the Company recommends against economic valve sizing. This is because most full port valves are not full pipe bore sized and reduced port valves have even smaller openings. The resulting increase in pressure drop across the valves means more pump and motor cost to drive the fluid through the lines. Other considerations become important, too: 1) what is the cost of installing reducers; 2) how much additional space is required; 3) does pipe stress need checking; and 4) can the system be drained?

Based on first quarter 1982 costs, if pipe lines are economically sized, ANSI Class 150 steel gate valves should usually be full line size for pipe diameters greater than 14 inches. Valve size will generally be smaller for higher pressure systems (i.e., Classes 300, 600, and 900) where valves are relatively more costly compared to pipe and fittings. The above assumes that reducers are located next to the reduced size valves with no intervening elbows or tees.

Block valves at control valves, pumps, and compressors should be at least one nominal size smaller than the line but not smaller than the control valve or pump flange. When the control valve or pump flanges are smaller than the line, no additional reducing fittings or welds are required with the smaller valves. Thus the economics of smaller valves is more attractive.

Valves smaller than line size should not be used in systems where excessive pressure drop cannot be tolerated, or where lines will be highly stressed due to thermal expansion.

For lines that have been sized based on available pressure, and not economics, block valves should be line size or one nominal size smaller. That is to say, in most cases after the line has been sized based on available pressure, there is generally enough pressure available to make the valves one size smaller.

For services where cast iron valves are permitted, valves smaller than line size generally cannot be justified economically and may be damaged by possible excessive line strains; hence they are not recommended.

Globe and angle valves smaller than line size are generally not economical because of the large pressure loss through these valves.

Reduced port plug cocks have a pressure loss equivalent to several velocity heads so it is seldom economical to make such valves smaller than the line. Also, for higher pressure ratings, plug valves cost less than gate valves so that possible investment savings are not as great. The economy of reduced size plug cocks of the full port type can be investigated in the same manner as for gate and ball valves, except the loss in the valve may be somewhat less than in a gate valve, say 0.05 velocity heads.

It is generally not economical to provide a reduced size valve if a tee preceding or following the valve must also be reduced size. Added pressure drop of the reduced size side-outlet tee will economically outweigh the cost savings of the reduced size valve. Where a reduced size valve discharges into the side connection of a tee, the tee should be full line size with two or three diameters of pipe between the reducer and the tee. On the upstream side of a valve, no straight pipe is needed between the tee and reducer.

The selection of pipe and valve sizes for steam flow is usually not based on economics. The pressure drop in steam headers must be low so that steam can be delivered throughout a process plant at its rated pressure. As a rule of thumb, pressure drop in steam lines is usually limited to 4 or 5 psi per 1000 feet for 150 psig steam and 1 or 2 psi per 1000 feet for 40 psig steam.

## Method of Analysis

As mentioned earlier, the determination of the economic valve size is fundamentally a matter of balancing the investment savings for the smaller valve against the increased cost of power required to overcome the pressure drop through the smaller valve. The incremental investment cost for pump and driver is considered insignificant since the increased pressure drop across the smaller valve will rarely result in a larger pump case. The added investment cost for electrical facilities is considered insignificant. To find the minimum cost, the derivative of the Total Annual Valve Cost (Equation 300-6) is taken and set equal to zero.

$$\frac{\delta \text{ (Total Annual Valve Cost)}}{\delta d} = 0$$

(Eq. 300-6)

The relation can be graphed for various valve diameters using the pipe diameter D as the ordinate and $QS^{1/3}$ as the abscissa.

In order to determine the desirability of using a reduced size valve, comparative costs of valves, flanges, reducers, etc., must be known for the various size valves.

The economic valve size is the one whose total comparable annual cost (installed cost plus energy cost) is the lowest. This can be expressed by the following equation:

Annual Cost = Amortized Installed Valve Cost + Energy Cost

$$= \frac{\text{Cost}_v}{r} + \frac{0.7457}{\text{eff.}} P_{\text{Loss}}[b + 8760\ c\ t\ ]$$

(Eq. 300-7)

where:

- r = Payout period, yr
- Cost$_v$ = Installed cost of valve, flanges, and reducers (if any), $
- b = Power demand charge, $/kw-yr

  *Note* &nbsp; *In some cases the demand charge is included with the rate charge. In these situations, "b" is not needed.*

- c = Power rate charge, $/kw-hr
- eff. = Combined efficiency of pump + driver,%
- P$_{\text{Loss}}$ = Power loss due to pressure drop through valves and reducers, hp
- t = % of year plant is in operation

**For Liquids:**

$$\Delta P = \frac{0.0011SQ^2}{d^4}(K_v + K_e)$$

$$P_{\text{Loss}} = \frac{Q\Delta P}{1715} = \frac{6.4 \cdot 10^{-7}SQ^3}{d^4}(K_v + K_e)$$

(Eq. 300-8)

**For Gases:**

$$\Delta P = \frac{2720}{d^4}(K_v + K_e)\frac{1}{\rho}\left(\frac{M}{100{,}000}\right)^2$$

$$P_{\text{Loss}} = \frac{M\Delta P}{13750\rho}$$

$$= \frac{19782}{d^4}(K_v + K_e)\frac{1}{\rho^2}\left(\frac{M}{100{,}000}\right)^3$$

(Eq. 300-9)

where:

- $\Delta P$ = Pressure drop through valve, psi

$P_{Loss}$ = Power loss through valve, hp

S = Liquid specific gravity

Q = Volumetric flow rate, gal/min

d = Valve inside diameter, in.

M = Mass flow rate, lb/hr

ρ = Fluid density, lb/ft³

$K_v$ = Valve velocity head loss coefficient

$K_e$ = Enlarger velocity head loss coefficient

The effect of viscosity is negligible.

The *Fluid Flow Manual* gives the loss in a fully opened regular gate valve as 0.2 velocity head. Actually, this $K_v$ value varies with valve size and among valve brands. Closer inspection shows that velocity head loss normally ranges from slightly above 0.2 for 4-inch valves to about 0.16 for 12-inch valves. The $K_v$ value then stays fairly constant at 0.14 for sizes above 14 inches.

For gate valves, use:

$K_v$ = 0.23 − 0.006 d, for d < 14 in.

= 0.14 d, for d ≥ 14 in.

These are conservative estimates, as most manufactures of good quality gate valves will claim lower head loss coefficients. The higher $K_v$ values were assumed to compensate for biased vendor data and to compensate for discontinuities at the flanges.

The head loss in an outlet reducer or taper may be expressed as a fraction of the loss of a sudden, square-corners enlargement. The loss in a sudden enlargement may be derived theoretically and is given by the familiar Borda formula,

$$h = \left(\frac{V_1 - V_2}{2g}\right)^2$$

(Eq. 300-10)

where:

h = head loss, ft

$V_1$ = initial velocity, ft/sec

$V_2$ = final velocity, ft/sec

g = acceleration of gravity

The sudden enlargement is equivalent to an included taper angle of 180 degrees and as this angle is decreased, the head loss first increases by about 20%, then decreases to the Borda formula value for an included angle of 40 degrees and reaches a

minimum loss for an included angle of about 7 degrees. This minimum loss is about 13% of the Borda formula loss. For most installations, however, a taper with an included angle of 7 degrees either consumes too much space or is too costly. Therefore, some valves are installed with outlet tapers having 12-degree included angles, but most are installed with standard reducer fittings with very large included angles. The velocity head loss coefficient for standard enlarger fittings is charted in the *Fluid Flow Manual*. An approximation for the curve is:

$$K_E = 1.7 - 2\frac{d}{D}, \text{ for } \frac{d}{D} < 0.8$$

$$= 0.5\!\left(1 - \frac{d}{D}\right), \text{ for } \frac{d}{D} > 0.8$$

(Eq. 300-11)

where:

K_e = Enlarger velocity head loss coefficient (based on d)

d = Valve diameter, in.

D = Pipe diameter, in.

It should be noted that the K_e values are based on the valve diameter d instead of the pipe diameter D, as were the values for K_v.

## 320 Layout and Arrangement

This section reviews equipment layout and piping practices common to most facilities. Sections 700 and 800 cover producing facilities.

Review and understanding of process and system hydraulic requirements are necessary for proper equipment layout and piping design. Established piping practices must then be applied to produce a safe design. An equipment layout and piping design that then balances operating, maintenance, and cost considerations should be the designer's goal.

An understanding of applicable codes and regulations is necessary when piping any facility. Standard Company practices meet or exceed piping code requirements for safety and fire protection; however, they must be reviewed in light of local laws and regulations. See Section 100 for a discussion of these laws and regulations and Company standards and specifications.

**On-plot vs. Off-plot.** In larger or more complex facilities, systems and equipment are generally grouped into hazardous and nonhazardous (or less hazardous) areas. These areas are typically labeled **on-plot** and **off-plot**. On-plot contains the operating or process facilities and off-plot serves to provide utilities, services and storage capacity in support of on-plot. The boundary line at the edge of the on-plot area is typically called the **plot limit** or **battery limit**.

In some installations there is no distinction between on-plot and off-plot; all facilities are grouped together. Examples include producing gathering stations, water injection plants, and offshore producing platforms where area separation is impossible.

## 321 Piping and Equipment Layout Development

### General

Site geography and the relative positions of facilities have an impact on pipe sizing and routing. For example, hillsides can be used to advantage for building impounding requirements and to provide gravity feed from tanks to operating areas or product tanks to loading areas. Prevailing winds must be considered when locating a facility if flammable, odorous, or toxic gases are a concern. Noise levels can also dictate the position of equipment and facilities.

Future expansion should be considered in the initial layout. Space should be left for future spare pumps, heat exchangers and pipeway capacity (about 25% of pipeway width).

Once the governing factors have been established for a given site, the equipment and facilities are normally grouped by function, as follows:

- Process facilities in one area (on-plot)
- Bulk storage of flammable materials remote from process areas, flares and fired heaters
- Support facilities like cooling towers, boilers, power generators and buildings, remote from fire-hazardous operating facilities
- Flares and vents separated from all other facilities

With the exception of power generators and buildings all these areas are interconnected by process or utility piping supported on pipeways.

### Pipe Routing

Within a given operating area, on-plot or off-plot, the simplest piping arrangement is usually achieved by placing equipment in sequential positions as determined by process or system flow requirements. Generally, the equipment is placed in rows on one or both sides of a main pipeway. Some equipment may be elevated for process reasons.

Elevated pipeways are preferred if space is at a premium. Grade level pipe prevents ready access to equipment. See Figure 300-5 for a typical on-plot process layout.

Sequential positioning of equipment is not always possible, especially with large or complex plants, or where more than one facility shares the same site. For example, the following factors can upset the orderly sequence of equipment layout, especially if space is limited:

![Fig. 300-5 Pipeway—Typical On-plot Process Layout](figures/01-overall-piping-design-standards-10_p0024_fig01_fig-300-5-pipeway-typical-on-plot-proces.png)

- Fired heaters and other direct-fired equipment should be grouped together, upwind from equipment with the potential for hydrocarbon leaks and easily accessible for firefighting

- Equipment requiring periodic cleaning or maintenance such as heat exchangers, fan coolers, and packed columns should be accessible to maintenance equipment

- Rotating equipment such as pumps, turbines, compressors and motors should be easily accessible for maintenance, often while the facility is in operation

- Powered equipment such as pumps is sometimes grouped together to save power supply installation costs

The best piping arrangement is seldom accomplished by connecting directly from one piece of equipment to another. Possible exceptions are small, remote or temporary facilities or cases where there is some particular process reason. Routing each line in a straight line creates a confusing and highly impractical arrangement.

An important rule is that branch lines serving equipment should always be perpendicular to the pipeway to which they connect. Piping should be arranged to run in definite patterns: from equipment to pipeway to equipment, changing directions with 90-degree turns. The more complex a facility is the more important this becomes.

Often plot plan studies of alternative piping arrangements reveal the best plant layout. Once equipment and pipeways are tentatively located using the above guide-

lines, the most expensive piping (alloy and/or large diameter) is routed on a preliminary plot plan. This keeps these runs short and economical.

The remaining pipe is then routed between equipment, using the pipeway. The pipeway area with the greatest density of pipe is identified in this fashion. This is called the **pinch point** and, with the addition of space for future lines, it dictates the width of the pipeway. See Section 324, Pipeways.

If space is at a premium, it is almost always possible to reduce the pinch point and pipeway width by relocating certain equipment and adding length to some piping. Once a layout is developed, the equipment piping connections, if not already established, can be properly oriented and sized.

## 322 Good Piping Practice

### Ground Rules

There are general piping practices that apply to almost all piped facilities, large and small, simple and complex. A list of these follows. More specific requirements involving operation, safety, and maintenance are discussed later. See also Standard Drawing GF-A1242.

1. Support all aboveground piping with grade level sleepers or elevated stanchions.

2. Minimize the number of flanges and unions to those needed for reasonable operation and maintenance; all are potential leak points. This is especially important in high-pressure systems and air quality-sensitive locations. See Section 240.

3. Provide ample space between lines in pipeways and around connected equipment to accommodate pipe, valves, instruments, electrical conduit, and workspace. This is discussed in detail later. Standard Drawings GC-L88505 and GD-L88506 provide piping dimensions and line spacing data.

4. Do not interconnect process and utility piping. When connections for flushing, steamout, or purging are necessary, always provide a check valve and a means of physically separating the systems when not in use—preferably a dropout spool, though plate blinds are commonly used. See Standard Drawing GD-L1012 and Section 100 of the *Utilities Manual*.

5. Always consider thermal expansion and flexibility. All lines are fixed at two points or more and must be designed to expand without overstressing themselves or connected equipment. This is especially true of rotating equipment, which is almost always sensitive to pipe-induced forces. See Section 330 of this manual.

6. Do not make flat turns. Change the line elevation when the line changes direction. This provides maximum flexibility in routing lines and in providing for future additional lines. Be wary of installing "pockets" that will not drain. Flat

turns are only acceptable in situations where there are very few lines and little possibility of future interference. See Figure 300-6.

![Fig. 300-6 Change of Pipeway Sequence](figures/01-overall-piping-design-standards-10_p0026_fig01_fig-300-6-change-of-pipeway-sequence.png)

7. Lateral connections should be made from the top of steam, vapor, and air lines unless condensate drainage is desired. Connections for liquid lines are typically on the bottom, but each case must be evaluated.

8. Install vents and drains. Piping should be designed with a minimum of high points that will trap gases and a minimum of pockets that will trap liquids. Where high and low points do exist, the system is usually provided with NPS ¾ (minimum) vent and drain connections. Typical applications and installations for operating, maintenance, and hydrostatic testing will be discussed presently. See also Standard Drawings GD-L31335 and GD-L1057.

9. Do not install **dead legs** in piping unless it is planned to extend the lines in the future. If support is needed add a **dummy** pipe extension to the nearest support. Dead legs can accumulate solids and open-ended dummy legs can trap water. Both are susceptible to internal corrosion. See Figure 300-7.

10. Minimize buried piping. Piping should be routed aboveground on supports. Burial may be necessary at road crossings, for protection from freezing or solar heating, and for fire protection. Buried lines may be more expensive, subject to corrosion, difficult to detect leaks in, and prone to future maintenance problems. See Section 350.

![Fig. 300-7 Dummy Leg](figures/01-overall-piping-design-standards-10_p0027_fig01_fig-300-7-dummy-leg.png)

## Operability

Operating personnel must be allowed to perform their daily tasks efficiently. Therefore, the most commonly used valves and instruments should be easily accessible, and sufficient space must exist between piped equipment so that personnel can pass quickly and freely through the plant. The following guidelines on clearances and accessibility are expanded and illustrated in the *Safety in Designs Manual*.

**Valving.** Valves that must be operated several times a day or shift should be accessible from grade. When this is not practical, access must be provided through the use of stiles, ladders and platforms, valve extension handles, or chainwheels. On the other hand, access to little-used drain valves from a kneeling position or vent valves from a ladder is acceptable.

Standard Drawing GB-L99961 illustrates the recommended options for mounting valves in almost all situations. Standard Drawing GB-L13963 provides details for fabrication of extension handles for rising stem valves. Valves should not be installed with the stem below horizontal because the bonnet accumulates debris and water, leading to freezing and corrosion.

Valve handwheel extensions and chainwheels are used only when no reasonable alternative exists. The mechanisms require maintenance and are subject to corrosion, and such valves are difficult to repack. Chainwheels are a nuisance, may not operate in an emergency, and can be a hazard if the chain is left off its tie-back and hangs in an accessway. NPS 2 valves are the smallest that should be considered for chainwheels.

**Clearances and Accessibility.** For access by operators and ease of maintenance, clear spaces of at least 30 to 36 inches must be provided around all equipment, including attached piping and neighboring facilities, and on platforms and stiles. If available, a clearance of four or five feet is not excessive. Pipe and equipment insulation thickness must also be considered when laying out the facility. Valves should

be given special care. The handwheel must be accessible (See the *Safety in Designs Manual*) but the stem should not extend into accessways. Early planning drawings should provide for 4-foot clearances until final layout drawings show that spacing can be decreased.

Major access aisles should be reasonably straight and free of random impediments such as pipe stanchions, valve handles, ladders, diagonal bracing, instruments, electrical boxes, chains, etc. Some aisles are used frequently for personnel and emergency access, and four-foot to five-foot widths are not unreasonable.

**Proximity.** Equipment, valves, and instruments that operate in conjunction with each other should be placed near or at least in sight of each other. Level gages should be visible from the associated level control valve and level control valve manifolds should be visible from the related level gage. In general, control valve manifolds should be near their actuating instruments, and any indicating instrument should be visible from any related manually controlled valve.

## Safety

**Fire Safety.** This discussion covers general piping and equipment layout as they are affected by considerations of fire safety. Detailed spacing requirements are covered in the *Fire Protection Manual*. Fire safety in relation to piping component use and material selection is covered elsewhere in this manual.

Fired equipment such as furnaces, boilers, and oil field heater-treaters should be kept separate from lines and equipment handling flammable fluids and upwind of relief valves venting to the atmosphere or other potential hydrocarbon sources. Fuel and snuffing steam block valves for fired heaters should be kept at least 50 feet from the heaters.

Pump seal failures are a common cause of fire. Pumps and other equipment handling flammable fluids should not be installed beneath platforms, structures, or pipeways. Overhead instrument or electrical runs should be routed around such equipment.

Pipe trenches should be avoided. They collect debris and promote corrosion. If unavoidable, adequate drainage must be provided.

Flanges and valves should be minimized in high fire risk areas. Remotely operated or thermal closing valves should be considered for critical service in areas where fire would prevent access.

Fire water piping systems in and adjacent to protected facilities should be buried to prevent freezing and ensure operation during a fire.

General facility layout considerations are reviewed in detail in the *Fire Protection Manual* and, in the case of tank fields, the *Tank Manual*. Fired heater piping is discussed below and in the *Fired Heater and Waste Heat Recovery Manual*.

**Mechanical Safety.** Mechanical safety and operability go hand in hand. Valve stems are a common problem. The safest arrangement is to install the valve in a horizontal line with the handwheel at a convenient elevation and the stem vertical.

When this is not possible the piping should be arranged so the stem does not project either diagonally or horizontally into areas needed for access, especially at head level. Acceptable valve positioning is discussed above in "Operability" in this section.

Clearances and valving around equipment requiring frequent maintenance such as pumps, turbines, and compressors deserve special attention because of the amount of time spent there by maintenance personnel, who need room for tools, spare parts, and machinery component laydown.

For mechanical strength the smallest pipe size recommended for all services other than instrumentation is NPS ¾. Some operating centers apply other standards and these are discussed in Sections 700 and 800.

Wear plates are recommended at pipe supports if there is frequent line movement due to thermal cycling or vibration, especially on thin wall piping. Insulated lines should have shoes in accordance with Standard Drawing GB-M99053.

**Relief Systems.** Relief valves that discharge into closed piping systems should be installed higher than their downstream piping. To prevent the formation of liquid slugs and for proper drainage, the complete relief system must continuously slope downward to the nearest liquid knockout drum. The minimum slope should be 2½ inches per 100 feet to effectively drain low spots created by the normal sag of lines between stanchions. This slope is the same as that recommended in API 521.

At times, the main relief header may be quite large in order to handle possible relief loads. This, combined with the slope requirement, can present special layout problems with respect to other plant piping. Lateral pipe must be routed over or under the relief header. The relief header is often the largest line and the highest line on plant pipeways; except for the relief valves that drain into the header. See Figure 300-8.

If more than one facility is discharging into a common relief system, each header may be provided with a locked-open block valve and, typically, a liquid knockout drum. In most cases the block valve is a single slide-gate valve with provision for blinding the header on the upstream side of the valve. Horizontal mounting of the valve is required, so that the gate cannot drop inadvertently. No other valves should be allowed in the system unless they can be locked open. Most operating centers have their own established practices. Variations in design practices are discussed in Sections 700 and 800.

Extreme changes of temperature and the need to handle liquid slugs during relief have an impact on the support and anchoring of relief systems. Proper sizing of closed pressure relief systems is covered in the *Instrumentation and Control Manual*. Support and anchoring of piping are covered in Section 330 of this manual. Relief valves that discharge directly to the atmosphere should be downwind of any fired equipment and provided with a vertical discharge line that vents at least 10 feet above any platform within a 25-foot radius.

![Fig. 300-8 Typical Arrangements of Relief Header and Lateral Lines](figures/01-overall-piping-design-standards-10_p0030_fig01_fig-300-8-typical-arrangements-relief-he.png)

## Ease of Maintenance

The two most significant factors in layout and piping design impacting maintenance are:

- Sufficient work space and access around equipment
- Sufficient valves, flanges, and blinds for proper isolation, cleanup, and testing of plant facilities

Where economically justified, permanently piped utility tie-ins can be installed in a facility. Standard Drawing GD-L1012 illustrates such connections for steamout, pumpout, purge, and flushing of piping and equipment. Section 100 of the *Utilities Manual* discusses the risk factors of such connections.

**Space and Access.** Where possible, equipment requiring periodic disassembly in the field, such as pumps, turbines, and compressors, should have sufficient space around it for tools, parts, and elbow room. Five or more feet is common.

Piping should not be routed over equipment unless there is a process reason. Clear overhead access should be provided for equipment handling. If this is not possible the piping should be flanged and removable spools provided.

Piping should not interfere with access to process equipment by maintenance equipment, including cranes. For rotating equipment provide access from above and at least one side. For heat exchanger bundle pulling, and fan and coil removal from filters and fan coolers, leave space at one end. For filters, vessels and columns with removable internals or packing leave space at one side.

**Isolation, Cleanup, and Testing.** Although their use should be minimized, flanges are required to remove piping for access to equipment, blind for pressure tests, and

to expose piping for inspection when necessary. The requirements and methods for these functions vary between operating centers.

Hydrostatic testing of lines and equipment can be done against closed valves, but the surest method of achieving a valid test is with plate blanks, or blind flanges. Standard Drawing GF-L99965 provides guidance for the blinding of refinery lines and equipment, but applies equally well to all facilities. Section 250 discusses blinding at flanges. Section 640 and Model Specification Industry Source 02 Doc MS-3541 cover pressure testing.

## 323 Manifolds

A piping manifold is an assembly of pipe, valves and fittings that gathers fluid from one or more sources and redirects it to one or more destinations. The term manifold is also applied to any assemblage of piping and valves grouped at one location for ease and convenience of operation. The latter category covers plot limit manifolds where all piping enters and leaves a plant, steam trap and sample draw manifolds, and even an individual control valve manifold with its block valves and bypass.

**Transfer/blending.** Figure 300-9 illustrates a typical oil field manifold installation, common in producing field-gathering stations, water injection stations, and in process plant off-plot product blending areas.

**Plot Limit.** Plot limit manifolds are groupings of isolation valves and blinds in the lines to and from a facility. They are generally located at the plot limit where, often, the main plant overhead pipeway drops into a grade level off-plot pipeway at a **waterfall**. Manifolds provide quick and safe operator access for plant isolation in the event of a fire or plant upset, and convenience during startup and shutdown. Small facilities may not use manifolds, instead installing block valves at the most convenient locations in the system. See Standard Drawings GF-A1247, GF-A1248, and GF-A1249.

Systems for which plant piping does not typically enter a plant at the plot limit manifold are cooling water, potable water, and fire water. These are normally buried for fire and freeze protection and do not shut down with the plant. System connections for washing, steamout, flushing, and purge are normally made at the plot limit manifold. These are shown on Standard Drawing GD-L1032.

Manifolds that are used daily are located at grade or accessed with stairs and platforms, depending on local practice or operator preference.

**Control Valve.** Unless specific process conditions govern, control valve manifolds should be located at grade (preferred) or on conveniently located platforms, with sufficient space on at least one side to service the valve and operator. Typical locations are against pipe stanchions and vessels. They should be in sight of instruments or indicators showing the variables they control.

Proper selection and sizing of control valves are discussed in the *Pump Manual* and *Instrumentation and Control Manual*. Control valves are typically installed with block valves and a globe bypass valve of the same size as the control valve. This allows continued system operation on manual control when the control valve is

![Fig. 300-9 Typical Oil Field Manifold Installation](figures/01-overall-piping-design-standards-10_p0032_fig01_fig-300-9-typical-oil-field-manifold-ins.png)

removed for maintenance. Some operating centers prefer to omit the bypass valve in noncritical service.

Properly sized control valves are usually one size smaller than the connected piping and are specified with flanges in all sizes for ease of removal. A plugged full-port NPS ¾ drain is usually installed between the control valve and the upstream block valve. Allow enough space between the drain and grade for plug removal and rodding the drain valve, which collects scale and debris. Standard Drawing GF-A1250 illustrates typical manifold configurations.

## Small Pipe

It is often convenient to group in one location small operation or maintenance functions that would otherwise be scattered throughout the facility. Examples are steam traps and sample draws. On off-plot pipeways NPS ¾ × 1 solar thermal relief valves are often manifolded together to a common discharge. Small piping is further discussed in Section 340 of this manual.

**Steam Trap.** Steam traps require periodic servicing and replacement. Routing all condensate lines in a given area from piping and equipment to one location greatly facilitates this. Typical steam trap manifolds are illustrated on Standard Drawing GD-L99596 (see the *Utilities Manual*). The application of steam tracing is discussed in the *Utilities Manual*.

**Sample Draws.** Process samples from overhead lines and equipment are often brought to grade and arranged in one location. In addition to operator convenience this allows sample drip disposal at one location and reduces the amount of cooling water piping when hot samples are involved. Typical sample draw configurations are shown on Standard Form Industry Source 02 Doc EF-403 and are discussed further in Section 340.

If grouping sample draws results in a long run from a sample point, the sample draw should be of the circulating type to ensure a true sample and eliminate the need to discard sample liquid. This requires discharging the sample stream to a point with lower pressure than the sample point. Tank sample draw manifolds are covered in the *Tank Manual*.

**Thermal Relief.** Multiple thermal relief valves are sometimes manifolded together. These are discussed in Section 340 and the *Tank Manual*.

# 324 Pipeways

This discussion is divided into on-plot and off-plot pipeways. The current trend is to place on-plot pipeways overhead and off-plot pipeways at grade. Where real estate is at a premium an elevated pipeway permits use of the space beneath it for access to equipment.

## On-plot Pipeways

On-plot elevated pipeways (see Standard Drawing GF-A1242) have advantages over those at grade level:

- The area under them is cleaner and clear of other plant facilities. Grade level pipeways collect debris, are difficult to clean, and restrict access to equipment and other plant areas
- The pipeway structure is a support for electrical and instrument distribution systems
- Stanchions serve as locations for electrical outlets, utility stations, firefighting equipment, first aid stations, and piping manifolds
- The piping is more easily drained and cleaned during shutdown

- Pipe insulation is better protected, and leak detection is improved

**Construction.** Typical pipeway stanchions are fabricated of steel. Where fireproofing is required it can be added per Standard Drawing GA-N33336 (in the *Insulation and Refractory Manual*) or reinforced concrete can be used instead of steel. Concrete stanchions should have imbedded steel bearing plates to support the piping. Pipeway design is covered, with examples of configurations, in the *Civil and Structural Manual*.

**Width.** Pipeway widths run from a few feet for small facilities to 50 feet with multiple decks for major plants. Establishing pipeway width is discussed in Section 320 under Piping Layout Development.

Once the actual space requirements are established it is common practice to add 25% for future changes and additions. A larger figure is used if the pipeway serves future plot area. Although it may not initially be obvious how this space will be used, hard experience has shown it to be necessary in most cases.

**Elevation.** Stanchions must be high enough to accommodate plant maintenance equipment beneath crossbeams, piping, area lighting, etc. Typical clearance for a cherry picker to handle pumps and large valves is 12½ feet. Firefighting equipment and commercial vehicles must also be considered.

On the other hand, stanchions should be low enough for maintenance on overhead valves, instruments, orifice meters, etc., and to allow all relief valves to drain to the plot limit knockout drum, if there is one. See Section 320. Figure 300-10 illustrates a typical pipeway stanchion elevation and shows that lines should not be placed directly over stanchions so that future decks may be added easily.

![Fig. 300-10 Single Deck with Elevated Relief Header—Typical](figures/01-overall-piping-design-standards-10_p0034_fig01_fig-300-10-single-deck-elevated-relief-h.png)

**Stanchion Spacing.** Stanchion spacing is a question of economics. Spacing is determined by the need for support of the majority of the lines in the pipeway. The smaller piping can be supported from intermediate supports between pipeway edge beams or sometimes from larger low temperature piping. Typical spacing is 20 to 25 feet. Stanchion spacing is covered in the *Civil and Structural Manual*. Figures 300-11 and 300-12 illustrate typical arrangements.

![Fig. 300-11 Stanchion Spacing—Small Pipe Requires Intermediate Support](figures/01-overall-piping-design-standards-10_p0035_fig01_fig-300-11-stanchion-spacing-small-pipe.png)

In naturally corrosive atmospheres such as at coastal refineries and offshore platforms, the use of U-bolts and clamps for small pipe supports is not recommended. Corrosion of the bolt threads and points of contact with the pipe is a continuous problem. Instead, welded supports or brackets that do not clamp the pipe are used.

![Fig. 300-12 Small Pipe Supported from Larger Lines or Intermediate Supports](figures/01-overall-piping-design-standards-10_p0036_fig01_fig-300-12-small-pipe-supported-from-lar.png)

**Edge Beams.** In most plants it is considered good practice to provide overhead edge beams connecting the stanchion columns. Edge beams provide the following benefits:

- Lateral bracing
- A continuous support system for electrical conduit and instrument cable racks (except over pumps)
- Support for lateral lines entering or leaving the pipeway
- Support for intermediate small pipe supports (already discussed under Stanchion Spacing)

**Arrangement of Lines.** The heaviest lines are placed near the columns to avoid excessive moments in the stanchion beams. Do not place lines over the columns if a future upper deck is a possibility. The upper practical limit for liquid-filled piping in overhead pipeways is NPS 18. Of course, structures can be built for any line size, but costs increase quickly.

Process and utility headers should normally be placed on the pipeway side where most of their lateral connections will be. An exception may be steam headers to turbines, which should be located on the opposite side of the pipeway to allow sufficient flexibility in the lateral steam lines. In plants with equipment on both sides of the pipeway, the utility headers will normally be in the center. If double-deck stanchions are used, the utilities are normally placed on the upper level.

**Line Spacing.** Standard Drawings GC-L8505 and GD-L8506 provide dimensional information for line spacing. Insulated lines require more space. When laying out piping, space can be conserved by staggering flanges.

**Intersections and Corners.** Generally, an elevation change is necessary at intersections and corners. This permits changes in line sequence when necessary and accommodates adding lines in the future. Flat turns at corners are **only** acceptable if the same line sequence is suitable in both pipeways, and if there is no chance that the corner will become an intersection in the future. See Figure 300-6.

**Expansion Loops.** Steam, condensate and hot process lines need room to expand and contract, and expansion loops are normally used. Expansion joints are not recommended on-plot. See Section 240.

Loops should extend over the pipeway, as opposed to the plant area, and be supported from the stanchions. They should be as close as possible to the center of the pipe run.

Typically loops are nested. Most pipeways have at least one critical line in terms of temperature, length, size, and (therefore) stress. Lines that undergo greater linear movement than the critical line should be placed inside this line in the loop system, and lines with less movement should be placed outside. Figure 300-13 demonstrates this.

![Fig. 300-13 Expansion Loop—Typical](figures/01-overall-piping-design-standards-10_p0038_fig01_fig-300-13-expansion-loop-typical.png)

**Anchors and Guides.** Additional flanges, dummy legs, guides, or anchor points may be required to restrain or guide the movement of hot lines or prevent transmittal of expansion stresses into equipment nozzles. See Section 330.

## Off-plot

Grade level off-plot pipeways are sized and developed in much the same way as on-plot. Greater width is often provided to accommodate line movement. Piping should be maintained at least 18 inches above grade on steel sleepers with concrete footings. Designs are discussed in the *Civil and Structural Manual*.

On pipeways that change direction and follow the natural terrain with elevation changes, small piping can be often allowed to "snake" in the pipeway, reducing the number of expansion loops.

Besides expansion loops, off-plot lines sometimes use expansion joints (slip joints). These are not recommended, especially in hydrocarbon service; they require maintenance and, being packed joints, have no fire resistance. See Section 240.

## 325 Rotating Equipment

All piped, rotating equipment has a common concern for sufficient access and proper valve location, pipe-induced stresses on the equipment, and the need for suction screens.

Piping systems for pumps, compressors, and turbines should be provided with sufficient flexibility and support so that forces and moments transmitted to the equipment do not exceed the maximums specified by the manufacturers. This is

especially critical with cast iron equipment. Flexibility design methods are explained in Section 330. Any grade level pipe supports should be adjustable and supported on a slab that is integral with the equipment foundation to eliminate differential movement.

Suction strainers are used primarily to catch debris especially in the suction piping of newly commissioned or modified systems. In the case of compressors they are especially important because of compressors' sensitivity to even the finest scale and grit. Although they are normally purchased, the fabrication of temporary suction strainers is discussed in Section 240.

## Centrifugal Pumps

For piping arrangement in congested areas, top suction/discharge pumps are preferred over side and end suction/discharge. Access space around large pumps should be greater than the three-foot minimum; use five to six feet for large multi-stage pumps. All pumps should be piped with suction and discharge block valves and a check valve mounted at the pump discharge.

Standard Drawings GF-L99958 and GF-L99959 demonstrate piping variations for end suction and top suction pumps. All these illustrations demonstrate a major rule: the general mass of pipe, valves, and manifolding is placed in a compact area in front of the pump.

Pump piping is usually larger than the pump nozzles. Valving at the pump should be the same size as the nozzles. If pump suction pressure is important, the suction valve should be line size.

Pump suction piping should be as short as practicable and have a minimum of bends to reduce turbulence. *A good rule is to provide five diameters of straight pipe into the suction nozzle, or two diameters if a reducer is also used.* The pipe between the block valve and suction nozzle should have a straight section long enough to accommodate a temporary suction screen. The piping should be designed so the strainer can be installed and removed without springing the pipe or otherwise disturbing pump alignment. Extra flanges and pipe supports may be needed.

Double-suction pumps are a special concern. Any right angle bend near the pump suction should be in the vertical plane to ensure balanced flow to the impeller. If this is not practical, five or more diameters of straight pipe should be installed, or the pump manufacturer consulted. Although not recommended, straightening vanes can be used in restricted areas.

Reducers in horizontal suction lines are normally installed with the flat side up to avoid trapping vapor and restricting flow. Flat-side-down reducers are acceptable when the liquid source is elevated and grit and solids could accumulate at the low point. If carried into the suction, these could damage the pump. This arrangement also eliminates the need for a drain connection at the low point.

## Reciprocating Pumps

Like centrifugal pumps, positive displacement pumps also require suction and discharge block valves, but not a check valve in the discharge. The piping is usually

located at grade to allow the better support needed for pulsing flow. Figure 300-14 is a schematic sketch of typical arrangements.

![Fig. 300-14 Reciprocating Pump Piping and Valve Arrangement—Typical](figures/01-overall-piping-design-standards-10_p0040_fig01_fig-300-14-reciprocating-pump-piping-val.png)

All positive displacement pumps normally have a pressure relief valve between the discharge nozzle and block valve. The relief valve should discharge to the suction source, usually a tank or accumulator. Relief into the suction line is less desirable, particularly if serious heat buildup can occur during circulation.

As with centrifugal pumps, temporary startup strainers are normally used and installed in a spool between the suction valve and nozzle.

Suction and discharge pulsation dampeners are often installed to reduce vibration in piping and equipment and to reduce the impact of acceleration head. Considerations of net positive suction head (NPSH) are unique for reciprocating pumps. See the *Pump Manual*.

On large reciprocating pumps, piping and dampener design require rigorous acoustical analysis. Although expensive, such analysis is usually cost-effective if it prevents redesign or lost productivity. See the *Compressor Manual* and the *Pump Manual*.

### Steam Turbines

This discussion is limited to single and multistage noncondensing turbines. The basic considerations in piping turbines are similar to those for centrifugal pumps, including the use of temporary startup suction strainers. Most turbines have side

nozzles, with the option of having both suction and discharge on the same side. Some models have vertical inlet nozzles. If the piping is simple, with no discharge pressure relief valve or APS (automatic pump startup, with a control valve in the inlet piping), having both nozzles on one side may be the best choice.

**Inlet Piping.** The inlet header and piping should be well steam-trapped to prevent condensate from entering the machine, especially on startup. This is particularly important for multistage turbines. Figure 300-15 illustrates good piping practice for a turbine with APS.

**Fig. 300-15** Steam Turbine with APS, Piping and Valve Arrangement—Typical for Single-stage Turbine

![Fig. 300-15 Steam Turbine with APS, Piping and Valve Arrangement—Typical for Single-stage Turbine](figures/01-overall-piping-design-standards-10_p0041_fig01_fig-300-15-steam-turbine-aps-piping-valv.png)

**Discharge Piping.** The discharge valve on most turbines is normally left open when the turbine is not operating, especially when an APS is installed. When the turbine is not operating, condensate collects and drains continuously through a case drain (provided on most turbines). If there is no case drain, piping downstream of the block valve must be steam-trapped. Some installations require a pressure relief valve to protect the turbine case exhaust when the discharge valve is closed. Figure 300-16 shows an acceptable discharge piping configuration.

When piping turbines, access must always be kept open to packing glands, lube oil connections and the governor. Acceptable arrangements are shown in Figure 300-17.

## Reciprocating Compressors

The typical reciprocating compressor is a horizontal cylinder machine and, depending on pressures, can be single or multistage. The suction nozzle is normally on top of the cylinder but can be on the bottom for air compressors. The discharge is on the opposite side. The American Petroleum Institute does not allow bottom

![Fig. 300-16 Steam Turbine Discharge Piping—Typical for Low Pressure Exhaust](figures/01-overall-piping-design-standards-10_p0042_fig01_fig-300-16-steam-turbine-discharge-pipin.png)

![Fig. 300-17 Steam Turbine Piping—Packing Gland, Lube Oil Connection, Governor Accessibility](figures/01-overall-piping-design-standards-10_p0042_fig02_fig-300-17-steam-turbine-piping-packing.png)

suction nozzles on process machines. Primary concerns with compressors are liquid carryover from suction scrubbers and entry of solid contaminants into the machine.

Reciprocating compressors are generally elevated to accommodate discharge piping. Larger units have platforms around them for access to the cylinders and suction piping. Although suction piping may be elevated for drainage back to a liquid knockout vessel, piping is kept close to the foundation level because of vibration and for ease of support.

Compressors, especially multistage units, have a great deal of auxiliary piping in addition to process piping. This and the need to disassemble cylinders necessitates allowing more space around them than for most other equipment. Typical auxiliary systems to be piped include N₂ purge systems for startup and shutdown, cooling water, dry air purge, lube oil circulation, and vent and drain collection.

The suction and discharge piping at each unit should have block valves. Suction and discharge piping for each stage should be kept short, have a minimum of bends, and drain away from the cylinder. Piping should be no smaller than the cylinder nozzle

sizes, and block valves should always be line size. Piping arrangement is further discussed in the *Compressor Manual*.

**Suction Piping.** Suction piping, including interstage suction piping, should have temporary suction strainers and provision for temporary pressure gages. Piping should not be pocketed and should slope back into upstream liquid knockout vessels. If this is not practical, the line should have a drain to remove any condensate that may collect against the block valve prior to startup.

Knockout vessels (scrubbers) should be fitted with mist eliminating pads to prevent carryover of liquid and solids, and located as close as possible to the compressor cylinder—within a maximum of 50 feet.

For most services it is advisable to heat trace and insulate suction and interstage suction piping between the upstream liquid knockout vessel and the cylinder to prevent condensation. This is not usually done for producing equipment.

In addition to temporary suction strainers, special precautions are taken in initially cleaning suction and interstage piping systems, including pulsation dampeners, between the liquid knockout vessel and cylinders. Typically an acid pickling procedure is used to remove all scale and grit. This procedure is described in Specification Industry Source 02 Doc MS-2411, as well as in Section 600 of this manual.

**Discharge Piping.** Normally, piping from the cylinder outlet to the next stage liquid knockout vessel is mechanically cleaned only. Intercoolers are often installed to enhance condensate removal and to lower gas temperatures for reasons involving personnel safety and piping materials.

**Pulsation.** The pulsing flow, pipe vibration and cyclic movement of reciprocating compressors can be a problem. With smaller units this is usually controlled by rigid support and anchoring of the piping. However, for units larger than 500 HP, or with discharge of more than 1000 psig, or for units operating in parallel it is good practice to make a formal pulsation analysis.

Industry Source 02 is a member of the Southern Gas Association (SGA) Program which, by arrangement with the Southwest Research Institute (SWRI), provides analysis of piping systems for attenuation of pulsations. This analysis typically results in adjustments to line sizes and lengths, and the evaluation of pulsation dampeners (also called surge bottles, volume bottles, and snubbers) in both suction and discharge piping. The analysis can include a design review of specific pipe and vessel supports and anchors. The *Compressor Manual* discusses this subject in Section 100 and in the various equipment specifications.

Pulsation dampeners are considered pressure vessels, not piping components, and must be installed as close as possible to the cylinder. This is discussed in the *Compressor Manual*. Figure 300-18 illustrates typical dampener arrangements.

## Centrifugal Compressors

These units are similar to multistage centrifugal pumps in principle but operate at speeds as high as 15,000 rpm and pressures to 5000 psig or more. The prime concerns are the same as for reciprocating compressors: liquid and solid carryover.

![Fig. 300-18 Dampener Arrangements—Preferred Strainer Locations](figures/01-overall-piping-design-standards-10_p0044_fig01_fig-300-18-dampener-arrangements-preferr.png)

In general, centrifugal compressors will tolerate more liquid in "mist" form than reciprocating machines, but still will not tolerate free liquid. Similarly, they will tolerate carryover of small quantities of solid particles—10 microns or smaller—without significant erosion. However, temporary suction strainers and liquid knockout vessels are still required.

To provide multistep compression, two or more casings are often mounted in series on one set of shafts with the driver. Intercoolers and liquid knockout vessels are installed, as with reciprocating compressors. As with reciprocating machines, ample space is needed for the many auxiliary systems requiring access, and to dismantle the machine and its piping. Figure 300-19 illustrates a schematic piping arrangement for such a two-casing system.

The piping nozzles are normally on the same side of the machine and are available face up or face down. Piping requirements are similar to those for reciprocating machines: line size block valves are used and the piping should drain away from the

![Fig. 300-19 Centrifugal Compressors—Two Casing System](figures/01-overall-piping-design-standards-10_p0045_fig01_fig-300-19-centrifugal-compressors-two-c.png)

compressor. However, volume bottles with additional pipe anchors and supports are not required.

On up-connected machines (nozzles on top) flanged breakout spools should be installed to allow removal of the machine for maintenance. For high-pressure, heavy-wall pipe these spools should be fitted in place and welded in the field to ensure proper alignment. Such spools should be fitted with lifting eyes for handling. Prefabricated spools often do not fit and can pull the casing out of alignment when bolted up. Piping arrangement is further discussed in the *Compressor Manual*.

**Suction Piping.** Liquid knockout vessels should be installed in the suction lines, with mist eliminating pads, and suction piping should be mechanically cleaned and/or air blown. In extreme cases of corrosion or scaling the lines are acid pickled. See Specification Industry Source 02 Doc MS-2411. The suction piping between the liquid knockout mist eliminating pad and the suction nozzle is typically heat traced and insulated to prevent condensation.

As with centrifugal pumps, the suction lines should have at least five diameters of straight pipe coming into the suction nozzle, with any suction strainer upstream of this pipe. A rigorous analysis of the aerodynamics of suction piping is given in the Elliott Company's *Centrifugal Compressor Inlet Piping—A Practical Guide*, which is included in the *Compressor Manual*.

Piping at the suction nozzle should contain a dropout spool for installation of the temporary startup strainer. Extra care should be taken in the selection of strainers for centrifugal compressors, as the perforated plate of the strainer is too light it is susceptible to rupture from solids buildup or vibration in the high velocity stream. The strainer should be bare perforated plate with no overlay of wire mesh screen.

**Discharge Piping.** Piping is installed and cleaned like piping for reciprocating machines. Intercoolers are usually installed for condensate removal. A check valve is added between the nozzle and block valve.

## 326 Fired Heaters

This discussion is limited to piping and pipeways leading to heaters. Detailed discussions of heater pass flow control, fuel control, burner piping, etc., are included in the *Fired Heater and Waste Heat Recovery Manual*.

For fire protection, heaters must be a safe distance from equipment such as pumps and compressors, where hydrocarbon leakage is most likely. Recommended distances are tabulated in the *Fire Protection Manual* for all facilities. This requirement generally places heaters at the edge of operating facilities and at the end of process pipeways. Wherever located, space is needed around them for pulling tubes, crane access, and firefighting equipment.

It is advisable to place the heater so that the pipeway does not point directly at it; an L or T configuration as shown in Figure 300-5 is best. This allows the maximum flexibility in tying the heater piping into the pipeway and allows for installation of additional units if necessary.

Easily accessible emergency block valves should be installed in the heater fuel and snuffing steam lines at least 50 feet from the units they serve.

In the case of fired boilers, local regulation often requires steam piping immediately connected to a steam generator to comply with the ASME Boiler and Pressure Vessel Code instead of the ANSI/ASME B31.1 Piping Code. This is discussed in Section 100 of this manual.

## 327 Columns, Vessels and Heat Exchangers

This section outlines basic good practices in piping of columns, vessels, and heat exchangers.

Where possible, piping arrangement alternatives for all equipment should be studied before piping connections and other accessories are located by equipment contractors. This allows development of the most straightforward and economical layouts. Once equipment piping connections are fixed, the piping designer may be forced into undesirable configurations to accommodate them.

Equipment pipe connections are almost always flanged. Exceptions are small-diameter screwed vent, drain, and instrument connections. Flanges allow isolation of equipment and piping for hydrostatic testing, plus equipment and pipe removal for access and inspection during shutdowns.

In some instances equipment must be elevated or spaced at unusually large intervals to accommodate the expansion of connected hot piping. Hot pump suction lines and vertical piping on columns require such special consideration. Piping flexibility, restraints, and supports are discussed in Section 330.

## Columns and Vertical Vessels

Refer to Standard Drawings GF-A1243 and GF-A1244 for general arrangements for these vessels. Piping design should be coordinated with the designers of the foundation and supports, ladders and platforms, and instrumentation. Skirt height should accommodate bottom piping head clearance at grade, unless the piping is brought to grade and stiles are used. High skirts better accommodate piping flexibility and pump NPSH requirements.

There should be crane access for handling column internals and packing, unless a davit mounted on the column top can handle it. Davits should swing clear of platforms, and set-down space must be provided at grade.

Ideally, manways (except the lower manway) are located away from the pipeway, with vertical piping grouped on the pipeway side of the column and platform and ladder access on either side. See Figure 300-20.

![Fig. 300-20 Manway Location Vertical Vessel Access](figures/01-overall-piping-design-standards-10_p0047_fig01_fig-300-20-manway-location-vertical-vess.png)

Ladder runs are limited to 30 feet between platforms. Platform and ladder design and applications are discussed in the *Civil and Structural Manual* and the *Safety in Designs Manual*.

Piping should not pass through platforms unless the platform is intended to provide blinding access for the piping, in which case maintain 30 inches of clear walkway around the piping. Instrumentation should be accessible from platforms, not from ladders. Place control valves at grade, if possible. See the *Instrumentation and Control Manual* for other layout considerations.

## Horizontal Vessels and Drums

Refer to Standard Drawing GF-A1246. Typical services for horizontal vessels are oil/gas/water separators, column reflux, surge, washers, treaters, liquid knockouts, and relief knockouts. The height above grade of a vessel bottom is normally dictated by the pump NPSH, water leg on the bottom, or need for clearance under piping (unless stiles are used). The vessel inlet and outlet are typically on opposite ends to obtain the longest residence time, with the inlet on top, and outlets on the top for vapor and bottom for liquid.

Controls and the majority of piping are grouped at one end. Pump suction is at the pump end of the vessel to shorten piping. The relief/vent connection normally is installed away from the inlet. Bottom water legs are located away from inlet turbulence.

## Heat Exchangers

**Shell and Tube.** The shell and tubing should be arranged with the channel section away from the plant, and with enough clear space to allow channel and bundle removal. If completed early enough, a review of piping study alternatives generally results in the best location and orientation of nozzles for the fabricator. It can also have an impact on exchanger process design that can benefit piping layout. Figure 300-21 illustrates a simplified piping design resulting from reversing the shell-side flow of an exchanger.

Exchangers in series are often stacked and connected with matching flanges coincident with the channel section. Three units high is the practical limit. Standard Drawing GD-L1050 illustrates the use of jack screws and blinds with stacked exchangers.

For heat exchangers, it is common piping practice to:

- Use flanged removable spools at channel sections to allow easy removal of channel and bundle

- Emphasize the importance of pipe flexibility analysis. Pipe-induced forces on flanges can contribute to body flange leaks

- Install piping and insulation with sufficient room for wrench clearance at body flanges

- In exchangers with cooling water (normally on the tube side), mount a flanged nozzle with valve between the cooling water inlet and outlet block valves to

allow flushing the cooling water side to the atmosphere while the plant is in operation

![Fig. 300-21 Heat Exchanger—Reversal of Shell-Side Flow](figures/01-overall-piping-design-standards-10_p0049_fig01_fig-300-21-heat-exchanger-reversal.png)

**Air Coolers.** Sometimes called **fin-fans**, air coolers should be installed to allow free flow of air into the underside of the unit. Typically mounted on legs at grade, they are also installed above pipeways in process areas. They should not be placed over hydrocarbon handling equipment, such as pumps or compressors, with a potential for leaks or fire. See Standard Drawing GF-A1242.

Air coolers are available with once-through or multipass design with flanged headers on each end. More than one bundle can share the same fan(s), with each bundle having its own inlet and outlet headers.

When laying out piping, the expansion and contraction of the tube bundles must be considered. Also, if the connected piping will impose any more than minimal forces on the nozzles, the manufacturer's design should be reviewed for adequacy.

## 328 Instrumentation

This section covers general practices in use of pipe for mounting instruments. Control valve manifolds have been discussed previously, in Section 323. Instrument applications and standard drawings of installation methods are included in the *Instrumentation and Control Manual*.

### General

Piped instrument connections from lines and equipment should be installed with root valves of the same pipe class and material as the line or equipment to which it connects. Consider using stainless steel needle valves in clean service.

Connections should be NPS ¾ minimum, except for orifice flange connections, which are NPS ½ in ANSI Class 300 through Class 600 flanges and should use ⅝-inch tubing.

Field instruments should be mounted in positions readily accessible from grade or a platform. The 30-inch minimum clearance requirement should be maintained on platforms.

### Flow Instruments

Meter runs should be given as much straight pipe upstream as practicable. Minimum lengths for various installations and services are reviewed in the *Instrumentation and Control Manual*. The orifice should be located upstream of any associated control valve and preferably be accessible from a platform if elevated.

Strainers should be installed upstream of all positive displacement meters—at a distance of 10 pipe diameters in the case of turbine meters. The strainer should have a valved blowdown connection and pressure gages to check efficiency. In services subject to two-phase flow, vapor eliminators should also be installed in the line. Refer to the *Instrumentation and Control Manual*.

### Level Instruments

Level instruments are generally mounted directly on vessels and columns. When supplementary instruments such as level gages and alarms are added the assemblies are often mounted on a bridle. Bridles are used to minimize the number of connections on a vessel and provide increased mechanical strength. This is reviewed in detail in the *Instrumentation and Control Manual*.

Typically, level controllers and gages on a vessel are independently mounted to provide independent readings. However, when a horizontal vessel diameter exceeds

six feet, the recommended method of mounting is as shown in Figure 300-22. This avoids excessively long individual connections. Level instruments should not share common connections with other services, such as fill, drain or pumpout lines, where flow can disturb readings.

![Fig. 300-22 Level Instrument Mounting—Horizontal Vessels Exceeding Six Feet in Diameter](figures/01-overall-piping-design-standards-10_p0051_fig01_fig-300-22-level-instrument-mounting-hor.png)

Gage glasses should have dedicated block valves and be fitted with vent and drain valves to allow in-place rodding and cleaning of the glass. Refer to the *Instrumentation and Control Manual* for specific applications.

## 330  Flexibility, Restraint and Support

### 331  Piping Flexibility and Stress Analysis

Piping is subjected to stresses from three different causes: hydraulic pressure, weight loads, and thermal expansion. These stresses will be considered in turn.

#### Sustained Pressure Forces

The forces exerted by a fluid under pressure create a hoop stress and a longitudinal stress in the pipe wall. The hoop stress is twice the magnitude of the longitudinal stress, and is the controlling criterion for pressure design of pipe. For calculation details see Pressure Design of Piping in Section 230.

## Sustained Weight Loads and Occasional Forces

A single span of pipe supported at two ends behaves structurally as a beam. Multiple connected spans form either a two- or a three-dimensional structural frame. The forces acting on pipe as a structural element are the weight of the pipe, the weight of the fluid, and the reaction forces from the pipe supports. The weights act as distributed unit loads, while the support reactions are concentrated forces. Other sources of additional distributed forces are wind loading, insulation, snow, and earthquakes. Additional concentrated forces can include valves and instruments installed in the line.

These forces can be divided into two categories: the **sustained forces** (weights of pipe, fluid, insulation, and valves or other attachments), and the **occasional forces** (wind loading, earthquake forces, and snow).

The stresses induced in the pipe by these forces can be characterized as **shear stress** at the supports, and **longitudinal stresses** from bending moments induced by weight loads. At midspan these longitudinal stresses are compressive at the top of pipe cross section and tensile at the bottom of the pipe cross section. On vertical runs of pipe, weight loads can cause compressive or tensile longitudinal stresses, depending on the location of the supports. A three-dimensional piping configuration can also develop a **torsional stress** loading in some of the piping members, depending on the location of restraints.

## Sustained and Occasional Stress

Stresses caused by sustained forces such as pressure and weight are referred to as sustained stresses, or primary stresses. They are typically not cyclic.

When excessive, sustained stress causes gross plastic deformation and rupture. This is because sustained stresses are not self-limiting; once plastic deformation begins it continues until failure occurs. Failures may occur without warning with a single application of the load. Such failures usually stem from pressure design failures.

**Allowable limits for sustained stresses** are related to the yield strength and to the ultimate rupture strength of the material. The allowable stresses vary with temperature and with the applicable section of ANSI/ASME B31. The allowable stresses are listed in tables that are part of the Code sections.

Stresses caused by occasional forces are referred to as occasional stresses. **Allowable limits for occasional stresses** per ANSI/ASME B31.3 are 33% higher than for sustained stresses.

## Expansion Stresses and Piping Flexibility

Piping systems undergo dimensional changes with any change in temperature. If the piping system is unrestrained it will freely expand without encountering any expansion stresses (also called **secondary stresses**). However, at the least, piping connections to equipment are generally fixed and act as anchors for piping. If the piping system is restrained by its terminals, guides or anchors (collectively called restraints), the action of the restraints will cause a buildup of stresses and some displacement of pipe from its original position.

The ratio of displacement versus stress buildup depends on the flexibility of the piping system. A flexible piping system has relatively free movement and little expansion stress buildup. A rigid piping system has very little movement (displacement) and high expansion stress buildup.

Unlike sustained stresses, expansion stresses are self-limiting; local yielding of the pipe at points of high stress concentration decreases the stress and stops further yielding. As a result of local yielding, a new equilibrium at the higher temperature and lower expansion stress level is established. When the system cools down the stresses reappear with an opposite sign and may again cause local yielding. A piping system subjected to a temperature cycle will go through a range of stresses commonly referred to as the **displacement stress range.**

Expansion stresses are usually attributable to thermal expansion and, typically, are cyclical. Because they are almost always self-limiting, a single application of the load does not produce a failure; failure is by fatigue after a (usually) high number of load applications.

Fatigue failures begin as a small crack at a stress riser or material imperfection on the inner or outer surface of the pipe. Poor or irregular welds are examples of stress risers. Leakage will generally occur before catastrophic failure, although simultaneous corrosion and expansion stress cycling can lead to a very rapid failure. Brittle materials are particularly susceptible to fatigue failure.

## Allowable Displacement Stress Range

The limit for expansion stresses is defined as the allowable displacement stress range and, for ANSI/ASME B31.1 and B31.3 Paragraph 302.3.5, is given as:

$$S_A = f (1.25 S_c + 0.25 S_h)$$

(Eq. 300-12)

where:

- $S_A$ = allowable displacement stress range
- $S_c$ = basic allowable stress at minimum metal temperature expected during displacement cycle
- $S_h$ = basic allowable stress at maximum metal temperature expected during displacement cycle
- $f$ = stress range reduction factor for displacement cycle conditions for the total number of cycles over the expected life

When $S_h$ is greater than $S_L$ (sum of longitudinal stresses due to sustained loads), the difference between them may be added to the term $0.25 S_h$. In that case the formula becomes:

$$S_A = [1.25 (S_c + S_h) - S_L]$$

(Eq. 300-13)

## The Need for Flexibility

Piping flexibility is necessary to keep pipe stresses within safe or specified limits and, more importantly, to protect connected equipment from damage by excessive forces or moments. Even if it operates at ambient conditions, piping connected to rotating equipment needs a certain degree of flexibility. The initial strain required to fit the piping may cause distortion of connecting flanges if the piping routing does not provide sufficient flexibility.

A piping system without adequate restraints, however, may become too flexible. Piping connected to reciprocating equipment is subjected to cyclic pressure loads that can cause vibration. In piping that is too flexible this vibration may attain amplitudes that are damaging to the piping. To reduce flexibility additional restraints, usually guides, must be installed in selected locations so as not to interfere with the thermal expansion of the pipe.

## Movement of Pipe at Supports

Freedom of horizontal movement may be provided by hangers or by sliding on the supports. The friction of sliding supports generally requires axial restraints on long lines to force line expansion in the desired direction, either into an expansion loop or towards an offset with a bend. Vertical movement may have to be assisted by spring hangers or supports. For example, inlet lines to steam turbines are commonly supported by springs to reduce the load on the turbine flanges.

Piping flexibility is usually provided through a careful planning of the piping layout that includes expansion loops or offsets where necessary. Piping flexibility achieved through piping layout alone is preferable to the use of expansion joints, since it requires less maintenance and eliminates the possibility of leaks caused by bellows failure.

## Flexibility Analysis

It is the usual practice to perform piping flexibility analysis for:

- NPS 3 and larger lines connected to rotating equipment
- Lines connected to reciprocating compressors
- Lines with temperatures of 600°F and higher

ANSI/ASME B31.3 requires no formal analysis for systems that (1) are duplicates or replacements without significant change of systems with satisfactory service records, (2) can be readily judged adequate by comparison with previously analyzed systems, or (3) are of uniform size, have no more than two points of fixation, have no intermediate restraints, and fall within the limitations of the following empirical equation from ANSI/ASME B31.3:

$$DY/(L-U)^2 \leq 0.03$$

(Eq. 300-14)

where:

D = outside diameter of pipe, in.

Y = resultant of total displacement strains to be absorbed by the piping system, in.

L = developed length of piping between anchors, ft

U = straight line distance between anchors, ft

This is the only simple inspection formula that can be offered, and it should be used with caution. ANSI/ASME B31.3 warns that there is no general proof that it will yield accurate or consistently conservative results. It is not applicable to systems used under severe cyclic conditions, and there is no assurance that terminal reactions will be acceptably low.

While design of piping for sustained stresses is fairly straightforward, analysis for expansion stresses is very complex. As mentioned previously, thermal expansion will not cause any stresses in pipe that is free to move. The magnitude of expansion stresses is a function of the restraints and of the flexibility of the piping system.

Flexibility is obtained using L- or Z-shaped offsets or U-shaped expansion loops. The L or Z offsets are usually part of the normal routing of the piping system. Plant layouts are usually designed to require offsets in piping routing. Expansion loops are introduced when flexibility resulting from normal offsets in the routing is not sufficient. Loop flexibility is obtained from the inherent flexibility of bends or elbows and from bending the straight sections of pipe between two elbows.

Piping flexibility and stress analysis can be performed by simplified methods or by computer calculations based on matrix methods:

- Simplified methods were developed for approximate stress calculations of the most common shapes. Most of these methods are limited to certain sizes and temperature ranges. The common limitation is the inability to calculate terminal loads. Simplified methods of analysis remained in wide use until the early 1980's, mainly because of the cost of computer time and the complexity of input into the matrix computer programs

- Matrix method flexibility programs for mainframe computers were developed in the 1960's

The development of PC-based piping flexibility programs in the mid-1980's, with user friendly input and graphic display of the piping models, has rendered the simplified methods obsolete. The PC-based CAESAR II piping flexibility program is site licensed to Industry Source 02. It requires an IBM XT, AT or compatible, with 640K memory, a math coprocessor, and a hard disk. CAESAR II is available from the ETD Technical Standards Division at $500.00 per copy.

The program is user friendly, with onscreen graphics for displaying piping models and reviewing the results. The program produces Code check reports for either ANSI/ASME B31.1 or B31.3. The program can model either fixed or gapped restraints, and tied or untied expansion bellows. The program can size and select spring hangers and spring supports. It can produce rotating equipment nozzle load reports. It can also calculate natural frequencies, and stresses caused by dynamic force-spectrum loads.

## 332 Pipe Supports and Hangers

Piping systems need to be supported to limit stresses in the piping at the support locations and also to limit reaction forces on the supports. See Standard Drawing GF-M99874 and Standard Forms CIV-EF-799 A to F and CIV-EF-79 for details of pipe supports. These documents are in the *Civil and Structural Manual*.

Spacing of supports or hangers is usually governed by the maximum deflection allowed by the material in the piping system, which, in turn, is governed by the need to provide free drainage. Supports for steel piping are usually spaced 20 to 25 feet apart on the main pipeways. Nonmetallic piping may require closer spacing. Lines NPS 1½ and smaller should also be supported halfway between these points. By definition, pipe supports act vertically and support the weight of the piping system.

## 333 Pipe Restraints

A pipe restraint is either a guide, a stop, or an anchor. A restraint is a device that prevents, limits or resists the thermal displacement of piping. Restraints are used to:

- Protect sensitive equipment
- Control movement of pipe
- Maintain separation between adjacent piping
- Direct thermal expansion into expansion loops

Restraints also help to isolate mechanical vibrations.

### Guides

A long pipe under axial compression is a weak column subject to buckling. To prevent buckling, lateral restraint (a guide) is used. Guides should not be placed near directional changes, where they would interfere with the flexibility of the piping.

### Anchors

Anchors are rigid devices that prevent translation and rotation of the pipe at one point so that the pipe is fully fixed in all axes. A flanged connection of pipe to a piece of equipment is an anchor. There are very few other anchor points used in piping systems.

### Stops

A stop prevents movement in the axial direction, but permits rotation of the pipe. In most cases a stop also acts as a support. Stops are frequently, but mistakenly, referred to as anchors. One needs to keep in mind the definition of anchors given above.

After designing anchors and stops, and determining the reaction forces, the piping designer should consult the structural designer about the adequacy of the pipeway structure.

## 340 Small Diameter Piping

### 341 General

Small diameter piping within the Company is defined as NPS 1½ and smaller, and large diameter piping as NPS 2 and larger. This is typical within the industry although NPS 2 is sometimes considered small diameter piping.

Because of the difficulty and cost of properly butt welding small diameter pipe, NPS 1½ and smaller piping is normally installed with threaded or socket weld couplings, fittings, and valves. Unions are used instead of flanges to assemble and disassemble the piping where the service or the piping classification allows.

With the exception of certain instrument piping and some vendor supplied auxiliary piping on equipment, NPS ¾ pipe is the smallest recommended size. In the normal course of operations and maintenance NPS ½ and smaller is considered too susceptible to mechanical damage. Root connections are of special concern because of the possible moments and stresses that can be imposed at the main pipe or equipment tie-in. Some operating centers take exception to the NPS ½ limitation in certain applications. This is discussed in Sections 700 and 800.

Tubing is not recommended in place of small process piping. Tubing materials and applications are discussed in Section 230.

Typical common small pipe services, with available references, are:

- **Vents and drains.** Standard Drawing GD-L31335, Section 320 of this manual
- **Sample draws.** Standard Form Industry Source 02 Doc EF-403, Standard Drawings GA-L31652 and GR-J1223
- **Steamout, pumpout, purge, and flush.** Standard Drawing GD-L1012
- **Steam tracing.** In the *Utilities Manual*, Section 700, Standard Drawings GD-L1066 and GF-L99888 and Standard Form UTL-EF-593
- **Condensate manifolds**
- **Condensate collection.** In the *Utilities Manual*, Standard Drawing GD-L99596 and Standard Form UTL-EF-303
- **Solar thermal relief. Section 340** of this manual
- **Utility stations.** Standard Form UTL-EF-308, in the *Utilities Manual*
- **Instrumentation.** *Instrumentation and Control Manual*
- **Equipment auxiliary piping.** *General Machinery Manual*, API Standard 614 and the appropriate equipment manual
- **Chemical injection systems**

## 342 Characteristics and Concerns

**Root Valves.** The strength of small diameter root valve connections is a prime concern. This includes vents and drains. The mass of the valve connected to a short length of small diameter pipe can induce undesirable stresses at the main line or equipment connection, especially in vibrating service. Appendix C of this manual, Piping Vibration Guidelines, discusses the general problem of vibration-induced fatigue in small branch, vent, drain, and instrument connections. It is a problem that must not be underestimated; fatigue failure of small connections has caused many spills, fires, and shutdowns.

How to recognize problems, and what practices to use to prevent failures are reviewed in Appendix C. See also Standard Drawing GD-L1057, Root Valve Installation. For pressure instruments in pulsating and vibrating services, see Sections 400 and 1600 of the *Instrumentation and Control Manual*. The following are some general guidelines:

- ANSI Class 3000 fittings (as a minimum) should be used to provide adequate structural strength
- Small connections should be challenged and eliminated unless necessary
- The root valve should be as close as possible to the pipe to which the branch, drain, vent, or instrument line connects
- Valves should have the minimum weight consistent with reliable design and ruggedness. Welded-bonnet valves are desirable selections for small gate valves
- A small branch connection cannot be expected to support massive piping layouts even with minimal vibration. The designer must consider the mass and lever arm effect of the entire branch assembly on the root connection
- Bridge welds should be used at all locations where vibration is suspected or where heavy root valves are unavoidable. See Standard Drawing GD-L1057
- Branch connection assemblies, particularly instrument leads, can be braced to the line for added support. The instrument itself, for instance, a pressure gage, can also be braced to the line
- Consider stainless steel tubing, not rigid piping, to connect small instruments to the root valve. However, piping should be used for level instruments. See the *Instrumentation and Control Manual*
- For additional safety in clean, high-pressure services, restriction orifice nipples can be installed in branch connections at root valve outlets, or restriction connectors used with instrument root valves, to limit stock flow in the event of branch line failure. Restriction fittings are shown on Standard Drawing GB-J123 in the *Instrumentation and Control Manual*. Consider using stainless steel male-by-female ¾ x ½-inch needle valves instead of gate valves and restrictor orifices; the cantilever effect of the needle valve is much smaller

**Seal Welding.** The primary reason for seal welding valves and threaded joints is to increase safety and mechanical strength. Stress concentration caused by exposed thread runout notches is thereby eliminated. Seal welding also minimizes leakage and accidental thread backoff. Seal welding is normally used in services where:

- The fluid is flammable (and the fire risk from leakage is high)
- The fluid is hazardous
- Vibration or thermal loads exist

Seal welding should cover all exposed threads with weld metal and should blend into the pipe as smoothly as practicable (see Standard Drawing GD-L1057 for details). Threaded joints to be seal welded must be made up dry, without thread compound or Teflon tape, **because these materials contaminate the weld and can release toxic vapors.**

Seal welding requirements vary in the Corporation Piping Specification. Low-pressure water and air services do not require seal welding. In Pipe Classes that require **limited** seal welding, selected joints are seal welded, principally the pressure side of the first valve off equipment or pipe headers. In Pipe Classes that require **complete** seal welding, all joints (except plugs in valved vents and drains, and instrument and tubing connections) are seal welded. See the Corporation Piping Specification.

**Bridge Welding.** In severe cyclic services the branch root connections should be made with short nipples (but not all-thread nipples) and multiple weld passes built up to the full hub diameter of the valve and for the full length of the nipple. For bridge welding details refer to Standard Drawing GD-L1057. Consider the use of top entry valves so repairs can be made without cutting the valve from the line.

Which applications require bridge welding versus seal welding should be given some thought. Bridge welding should be considered for critical services only. The additional field labor required is expensive. Also, special precautions may be necessary to protect valves from heat while welding. This is described on Standard Drawing GD-L1057.

Suggested applications for bridge welding of small root valves are:

- Systems with flange ratings above ANSI Class 900
- Steam and boiler feedwater service at 600 psig
- LPG and H₂S services
- Vibrating service involving reciprocating and rotating equipment

**Threaded Connections Versus Socket Welding.** Threaded connections for NPS 1½ and smaller pipe are usually less expensive than socket welded connections, but have the following disadvantages:

- Weakness resulting from the notch effect at the root of the thread which localizes the effect of imposed stresses, promoting fatigue failure
- The decrease in effective wall thickness where threads are cut
- Susceptibility to thread disengagement by expansion when exposed to fire

- Inability to properly seal weld joints once pipe dope or Teflon tape is used

Where exposed threads are not acceptable, joints should be socket welded or threaded and seal welded. Both are considered the equivalent of butt welded or flanged joints for fire safety. Economics should govern the choice between them. Figure 300-23 shows comparative times to field fabricate and erect NPS 2 and smaller pipe using various methods.

**Fig. 300-23** Field Fabrication Methods Comparison—Small Pipe

> **Table - Fig. 300-23 Field Fabrication Methods Comparison—Small Pipe** - see [XLSX](tables/01-overall-piping-design-standards-10_p0060_tbl01_fig-300-23-field-fabrication-methods-com.xlsx) and [source crop](tables/01-overall-piping-design-standards-10_p0060_tbl01_fig-300-23-field-fabrication-methods-com.png)

| Joint Type | Hours per Linear Foot |
| :--- | :---: |
| Screwed | 0.4 |
| Screwed & Seal weld | 0.7 |
| Socket weld | 0.6 |
| Butt weld | 0.9 |

With socket welded construction, vents and drains should use screwed valves or valves with one socket weld connection and one screwed connection.

All open ended connections to flammable fluid systems such as drains, vents, unused instrument connections, etc., should be fitted with threaded solid bar stock plugs of the same material as the connection. Bar stock plugs should have a shank equal in length to at least twice their diameter to accommodate pipe wrenches (hex head plugs will not withstand repeated use). Free machining steels (high lead or high sulfur content) should not be used for bar stock plugs because they are subject to corrosion and cannot be seal welded.

## 343 Pipe, Fittings and Connections

**Pipe.** To ensure adequate mechanical strength, ANSI/ASME Code B31.3 requires Schedule 80 minimum pipe for NPS 1½ and smaller. In dirty, waxy, or high pour point services or services subject to freezing, line size should be selected with care. For example, NPS 1½ might be required over NPS 1 to protect against plugging.

**Fittings.** Forged carbon steel fittings should be used in all hydrocarbon services. Poor weldability and inconsistent quality "free machining" and "cold rolled" steel bar stock fittings are not acceptable.

Threaded bushings are **inacceptable** because their reduced thickness at the thread roots makes them susceptible to fatigue cracking at that point. Most operating centers have stopped using them. Swaged nipples should be used to change sizes in threaded piping.

In piping classes that allow cast iron valves and fittings, use Class 150 or Class 300 ductile or malleable cast iron, or Class 300 ductile cast iron threaded fittings. Do not use gray or white cast iron; they are **excessively** brittle. See Section 220.

**Flanges.** Socket weld or butt weld flanges should be used for steam above 150 psig, and LPG, hydrogen, or hazardous services where thermal cycling is anticipated. See Section 250 of this manual for further discussion.

**Unions.** Unions should be specified with metal-to-metal seats. They are most commonly used in low-pressure hydrocarbon and utility services to 150 psig.

The standards for malleable iron and carbon steel unions are ANSI B16.39 and MSS SP83, respectively. These standards do not specify seat construction, seat dimensions, or closure nut thread diameter. Each manufacturer sets his own dimensions and thread type for the coupling nut. As a result, union parts from different manufacturers are not interchangeable and any replacements should be done on a like basis. Used union parts from the same manufacturer should not be reused without lapping the seating surfaces. It is recommended that each operating center standardize on one manufacturer to avoid problems of mismatching or noninterchangeable parts.

Because of their brittleness **white** or **gray** cast iron unions should **not** be used; malleable or ductile cast iron should be specified. Forged carbon steel should be used in all hydrocarbon services.

## 344 Thermal Relief Piping

Thermal relief valves are required on all liquid-packed lines where valves may be closed on both ends of a line section during normal or abnormal conditions. Properly locating thermal relief valves and calculation of solar pressure rise is covered in the *Instrumentation and Control Manual*.

A typical thermal relief installation is shown in Figure 300-24. Observe that the root valve is a **globe valve**. This allows the **small pipe nipple** to be placed on the stem as a lockout device. This is not possible on OS&Y gate valves because of their non-rising handwheel. Gate valves can be chained or wired open with braided stainless steel rope and secured with a car-seal. Use of ball valves is discouraged, but, where used, they should be purchased with lockout trim on the bonnet.

Several relief valves may be manifolded together to a common drain header. Drains usually lead to a tank, vessel or other appropriate containment system. Open drains to atmosphere are usually limited to clean, nonhazardous, nonpolluting services. Closed drains may require an inlet valve on the drain header, also with lockout. Manifolded reliefs are not recommended if stock contamination is possible. Fluid from higher pressure or higher elevation systems can enter other systems if the relief valves are leaking.

## 350 Buried Piping

This section discusses buried steel pipe only. Drainage piping is covered in the *Civil and Structural Manual*, and nonmetallic pressure pipe is covered in Section 400 of this manual.

**Fig. 300-24** Typical Thermal Relief Installation

![Fig. 300-24 Typical Thermal Relief Installation](figures/01-overall-piping-design-standards-10_p0062_fig01_fig-300-24-typical-thermal-relief-instal.png)

Piping should not be installed underground when it can reasonably be avoided. Although there is good reason to do so in many instances, it is expensive and introduces problems not encountered with aboveground installations.

Underground piping is most often associated with cross country pipelines and marketing operations where security and safety justify burial. Additional applications are fire protection in operating centers, protection of water piping from freezing, mechanical protection of critical lines in operating areas, and road and rail crossings. Refer to the *Pipeline Manual*.

## 351 Problems Associated with Buried Piping

The principal problem with buried lines is external corrosion and the potential for undetected stock loss and ground water/soil contamination. Other related problems are the inability to drain or clean lines, to detect leaks and repair them once discovered, and to modify or make piping connections.

Buried lines are always subject to mechanical damage when being excavated or if excavation work is being done nearby. This is true even if accurate records of their location and depth have been preserved. Abandoned buried lines almost always become problems.

Risk of mechanical damage can be reduced if a ribbon of colored inert plastic tape is buried a few feet above the line. The tape alerts anyone excavating that a line is located beneath it. The tape can be purchased with a continuous printed message identifying the line, and with a metallized foil lamination to allow locating buried plastic pipe with metal detectors.

Hot buried lines present additional problems involving thermal expansion and the high temperature effect on the coating. Lines installed at ambient temperatures and

operated at higher temperatures are subject to compressive stresses. Adequate coverage and restraint must be provided to prevent buckling or line movement. This is discussed in the *Pipeline Manual*. Section 350 includes a summary of temperature limitations of coatings.

## 352 Corrosion Protection of Buried Piping

**Coatings.** With the possible exception of cast iron piping in drain line service, all metal piping installed underground should be protected from soil corrosion with a suitable coating. The *Coatings Manual* contains a detailed discussion of the merits of available coatings and wrappings, with their applications, limitations, and relative costs.

The following is a list of the most commonly used acceptable coatings and wrappings with approximate temperature limitations:

- **Fusion bonded epoxy**—below 200°F
- **Liquid epoxies**—below 225°F
- **Extruded plastic**—below 180°F
- **Tape wraps**—below 140°F (high temperature thermosetting tape available)
- **Coal tar enamels**—below 140°F
- **Somastic**—120°F to 212°F (four grades)—not readily available

Once commonly used in general service within the Company, "P2" asphalt wrap coatings are no longer recommended. Their performance has been poor compared to other coatings.

When small quantities of buried piping require protection, tape wrap is often selected because it is relatively inexpensive and easy to apply in the field. However, it is often the least reliable coating, with poor performance in water- and oil-saturated soils, and in cyclic temperature service. It requires proper pipe surface preparation and is easily applied improperly.

Protection for coated pipe at weld joints and tie-ins is provided by field-applied fusion bonded epoxy, shrink sleeves of polyethylene, heat-cured liquid epoxy, or tape wrap. Compatibility of these materials with the various pipe coatings is discussed in the *Coatings Manual*.

Aside from the type of coating selected, proper application of the coating and maintenance of its integrity are required for proper installation of a protected line. Because success or failure cannot be determined for an extended time after installation, usually years, attention should be paid to:

- Correct surface preparation for the type of coating used
- Application of the coating to the specified consistency and thickness
- Care in handling and laying to avoid coating damage
- Proper cleaning, priming, and field coating of joints and fittings
- Inspection of coating for any damage and proper repair

- Backfilling and compacting to prevent contact with any material that could damage the coating

These concerns and appropriate procedures are discussed in the *Pipeline Manual* and the *Coatings Manual*.

**Cathodic Protection.** Cathodic protection (CP) can be roughly defined as retarding or preventing the corrosion of a metal by imposing an electrical current flowing to the metal through an electrolyte. In the case of buried piping, the pipe is the metal and the soil is the electrolyte.

The basic principle of cathodic protection is quite simple, but the applications can be very complex. A thorough discussion of design and application is included in the *Corrosion Prevention Manual*.

Cathodic protection is often used with coatings to protect piping. Regardless of the care used in coating and installing buried lines there will often be small pinholes, or "holidays," in the coating. A cathodic protection system can protect against corrosion at these points and significantly extend the life of the piping.

Cathodic protection is applied to underground piping as a system. At every location where cathodically protected pipe leaves the soil (or water) it must be electrically isolated from the aboveground continuation of the line if the continuation is not part of the CP system. This is done with an **insulating flange kit** (or insulating union on small diameter pipe) that uses electrically insulating bolt sleeves, nut washers, and sealing gasket in a conventional flange makeup. Figure 300-25.

**Fig. 300-25** Insulating Gasket Set *Courtesy of The Flexitallic Group*

![Fig. 300-25 Insulating Gasket Set Courtesy of The Flexitallic Group](figures/01-overall-piping-design-standards-10_p0064_fig01_insulating-gasket-set-fig-300-25.png)

Producing piping, cross country pipelines, and submarine piping are the principal users of cathodic protection. It is also used to protect steel marine piling, offshore drilling and producing structures, ship hull exteriors, and tanker interiors. With the possible exception of protecting tank bottoms, cathodic protection is seldom used in refineries.

Care must be taken when designing a CP system to protect coated piping. Excessive current flow can result in **cathodic disbondment** of the coating from the metal at points where the coating is damaged, resulting in further deterioration of the coating. This phenomenon is discussed in the *Coatings Manual* and the *Corrosion Prevention Manual*. Because of excessive power requirements and difficulty in uniform distribution of protection, cathodic protection is rarely applied to bare piping.

**Casings.** Pipe crossings beneath roads and railroad rights-of-way, in addition to being coated, often must be sleeved in a casing. Casings are generally a local requirement of the right-of-way owner or the governing jurisdictional body. The design and installation of casings is discussed in API Recommended Practice 1102, *Recommended Practice for Liquid Petroleum Pipelines Crossing Railroads and Highways*, and in the *Civil and Structural Manual* and the *Pipeline Manual*.

LPG piping through brick or concrete walls and through earth fills, such as road crossings and embankments, should be protected by oil-filled casings treated with protective coatings. The oil-filled casing gives extra protection to the LPG line and allows leakage to be detected by pressure gages on the casing before it reaches the atmosphere.
