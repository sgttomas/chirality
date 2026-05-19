[Industry Source 03 logo]

# Table of Contents

1. **Objective** ...................................................................................................... 5
2. **Design and Application** ................................................................................ 6
3. **Emergency Isolation** ..................................................................................... 6
   - 3.1 Shutdown Valves ..................................................................................... 6
   - 3.2 System and Equipment Isolation ............................................................. 7
   - 3.3 Industry Source 03 Processing Facility (NPF) Battery Limit Isolations .................. 8
4. **Shutdown** ...................................................................................................... 8
   - 4.1 Shutdown Levels ..................................................................................... 8
     - 4.1.1 Local Shutdown (SD) ......................................................................... 8
     - 4.1.2 Unit Shutdown (USD) ......................................................................... 8
     - 4.1.3 Process Shut Down (PSD) ................................................................. 9
     - 4.1.4 Emergency Shutdown (ESD) ............................................................. 9
     - 4.1.5 Total Plant Shutdown (TPS) ............................................................... 9
   - 4.2 Critical Equipment ................................................................................... 9
   - 4.3 Minimization of Shutdowns ..................................................................... 9
5. **Depressurization** .......................................................................................... 10
6. **Attachments** .................................................................................................. 10

# 1 Objective

The purpose of this document is to identify the minimum design requirements for Emergency Isolation and Shutdown of the Industry Source 03 Processing Facility. The ability to progressively shutdown energy sources, isolate hydrocarbon inventory, and depressure the process system is the preferred method of protecting hydrocarbon processing facilities.

The hierarchy for system control and loss prevention is:

1. Process Control System (PCS)

2. This system is designed to keep the system operating in its normal operating conditions and set-points. During transient conditions, it is designed to control the system back into normal operating state.

3. Safety Instrumented System (SIS)

4. This system is designed to respond to instrumentation in the process equipment, typically when process conditions exceed certain setpoints, such as high-high pressure, or low-low level. If the process control system is not able to respond to the transient condition, and the process reaches high-high or low-low levels, the SIS will shutdown certain equipment, systems, or the entire process, until a safe condition is met.

5. Mechanical Relieving Devices

6. If the PCS and SIS are not able to respond or contain a transient condition, particularly high pressure, mechanical relief devices are provided as an additional level of protection.

7. Fire & Gas Systems

8. If there is a mechanical failure in the system, leading to a leak and/or fire, the fire and gas systems will trigger alarms, and ultimately lead to a confirmed fire or confirmed gas signal. A confirmed gas or confirmed fire signal from the Fire & Gas system will trigger a shutdown and depressurization of affected systems through the SIS. In applicable modules, the fine water mist system may be started through the Fire & Gas system, or the SIS, or both.

9. Manual Operator Shutdown

10. Operations can initiate a shutdown and/or depressure of individual systems or of the entire facility. This occurs when the previous 4 safeguards do not completely contain or shutdown the systems as

required. This shutdown is typically pushbuttons located in the control room and in strategic locations within modules.

The scope of this document is limited to items 2, 4 and 5 above.

The SIS in conjunction with the PCS is also the primary protection against the escalation of materials release and propagation of fire. In the event of a fire, the SIS is engineered to isolate and depressurize the affected areas and systems to reduce the stress on equipment to maintain containment of flammable process fluids within the systems, or safely evacuate the flammable materials through the flare stack.

Further information about the blowdown system is included in document Industry Source 03 Doc PRPHL-000001 *Relief and Blowdown Philosophy*.

# 2 Design and Application

The SIS designed for this facility shall be designed to be fail-safe, with included redundancies as necessary for the application. The primary requirements for the SIS are:

1. Safely stop the flow in an emergency condition.

2. Isolate systems, vessels, equipment, pipelines, etc. as necessary

3. Provide safe shutdown of equipment

4. Initiate blowdown/depressurization as necessary

In the event of Process or Plant Shutdown, the SIS system will communicate with all affected outside systems such as Drillsites, Campsite, etc. for notification or appropriate actions as needed.

# 3 Emergency Isolation

## 3.1 Shutdown Valves

Emergency Isolation of the Process Systems shall be achieved with automatic shutdown valves. These valves shall be designed with appropriate fail-safe considerations, and designed to withstand an upset and emergency condition, including:

1. Process pressures and temperatures during the upset condition

2. Fire (fire safe); explosion, chemical exposure from release of hydrocarbons or other hazardous fluids from nearby equipment or process lines

3. Valve to move to, or remain in, the safe position (fail safe) upon emergency isolation condition and upon removal of electricity, control signal, instrument air, hydraulic lines, etc.

4. Valve should also open/close in a time frame appropriate for the system, the valve shall actuate quick enough to safety isolate the system in time to minimize damage, but delayed enough to avoid equipment damage due to pressure surge.

Isolation valves should also remain in safe position following an emergency isolation until locally reset and repositioned. Local reset or a reset from the DCS which should be programed to allow resetting of Shutdown and Isolation valves in a specific sequence without software override. If done out of sequence, password protected override should be used.

There may be additional requirements or exceptions, such as the need for certain shutdown valves requiring the ability to perform partial stroke test online, but all these will need to be reviewed case-by-case.

## 3.2 System and Equipment Isolation

Emergency isolation valves shall be provided at the inlet and/or outlet process equipment at the following locations:

1. Upstream of any Equipment (Vessels, Pumps, Compressor, etc.) that has upstream equipment that has a higher design pressure or temperature.

2. On the liquid outlet downstream of vessels containing significant amounts of liquid hydrocarbons

3. At the Suction and Discharge of every compressor train, or pump trains, processing hydrocarbons or other hazardous fluids.

4. If the compressor/pump train includes dedicated: scrubber vessel(s), cooler(s), pulsation dampener(s), or other equipment, only one set of shutdown valves are required and are placed upstream of the first piece of equipment in the train, and downstream of the last piece of equipment in the train.

5. If the compressor/pump train includes multiple stages, interstage emergency isolation valves are required if the piping and equipment design pressure changes between stages, or if the normal operating liquid level within the stage is a significant volume.

6. Fuel feed to users, including gas turbines, fired heaters, power generators, etc.

## 3.3 Industry Source 03 Processing Facility (NPF) Battery Limit Isolations

Isolation valves must be provided for the overall plant feed and export lines at or near the battery limits. Isolation valves will need to be provided for any imported hydrocarbon streams such as fuel gas, makeup gas, etc. Isolation valves will need to be provided at hydrocarbon export lines, including the crude sales line, and any fuel gas export lines, and lift gas and injection gas lines, in addition to any pump or compressor discharge valves that may exist. Compliance with EIS requirements is required, such as the need to add ESD valves at major river crossings on export crude lines.

# 4 Shutdown

During an emergency or transient condition, in addition to system isolation, the SIS will also trigger equipment shutdown, depending on the emergency or transient condition. Within a system the equipment will generally be triggered to shutdown, which may involve an instantaneous removal of power, or a controlled slow down to stop, or in the case of critical utility or safety related equipment, may still fully operate even during an emergency shutdown, such as electric generators, fire and gas systems, etc.

## 4.1 Shutdown Levels

These shutdowns are listed below in order of smallest shutdown with least impact, to most significant shutdown involving total shutdown of the facility. Each higher shutdown level will trigger the shutdown the respective lower level shutdowns. For example, a particular Unit Shutdown signal will trigger multiple Local Shutdown signals associated with that Unit Shutdown, such as a compressor system shutdown (Unit Shutdown) will trigger the shutdown of the scrubber pump and compressor lube oil pumps (Local Shutdowns) associate with that system.

### 4.1.1 Local Shutdown (SD)

Local Shutdown is designed to isolate and protect as single piece of equipment or section of the system. It is applied in cases where shutdown of a single piece of equipment does not necessitate a larger shutdown. An example of a single equipment shutdown is for a pump motor winding high temperature shutdown when a spare pump is present and can be turned on.

### 4.1.2 Unit Shutdown (USD)

The USD is an Automatic or Manual shutdown of a group of equipment or a process system. The USD is designed to isolate a group of equipment or process systems due to an unsafe operating condition, such as an over-the-limit operating pressure, temperature, flow, or level, which will trigger an automatic unit shutdown. The NPF will be divided into process systems that allow for safe shutdown of the individual unit, while allowing other systems to maintain operation, possibly at a lower capacity. An example is

shutdown of a compressor station (all Flash Gas, or all Lift Gas, or all Injection Compressors as a group). Another example is a shutdown of the HP or LP fuel gas system. This shutdown trips the next lower hierarchy or local shutdown.

### 4.1.3 Process Shut Down (PSD)

The PSD is an Automatic or Manual shutdown of the entire NPF Process System, while maintaining operation of utilities and electrical generation capabilities. An example of a condition that might trigger a manual shutdown could be a leak or loss of pressure containment that is detected during a field walkdown. The PSD will not automatically trigger a blowdown, but provisions are provided in the control room to manually blowdown after a PSD if required.

### 4.1.4 Emergency Shutdown (ESD)

Emergency Shutdown is triggered by manual ESD pushbutton at the module exits and in the control room, or by confirmed fire or gas detection. This will trigger isolation and shutdown of the entire NPF and well pads. Confirmed fire or gas will trigger automatic blowdown, however the ESD pushbutton by Operator will not automatically trigger a blowdown, but provisions will be provided in the control room to blowdown the affected areas as required.

### 4.1.5 Total Plant Shutdown (TPS)

Manually initiated shutdown located in the control room triggers an automated shutdown entire NPF process systems, utilities, and power generation systems. The TPS does not automatically trigger a blowdown of the facility, but provisions will be provided in the control room to blowdown the affected areas if required.

## 4.2 Critical Equipment

Within a system, non-essential rotating equipment are typically shutdown during an emergency isolation to deenergize the system. The shutdown method depends on the equipment and the manufacturer's recommendations.

Some essential equipment may remain energized despite a system or total plant shutdown, if the equipment is critical for emergency operation. The two common examples of this is a firewater or fine water mist pump, standby generator sets, and instrument air, which will be designed to remain operable despite a shutdown.

## 4.3 Minimization of Shutdowns

The shutdown system and hierarchy shall be designed to minimize the number of equipment shutdown during a particular event. During a shutdown event, the shutdown shall be minimized to the smallest

shutdown listed in Section 4.1 that would contain the event. If a local equipment shutdown would be sufficient to contain the fault, this shutdown should be used, and maintain the remainder of the plant in normal operation, potentially at reduced throughput. The design of the SIS in conjunction with the PCS should consider the effects of shutdown on the affected system and any potentially affected systems to ensure one isolated shutdown does not cause cascading shutdowns of other systems unnecessarily. For example a trip of one the gas lift compressor will result in high pressure in the inlet separator. The PCS will open the back pressure valve to HP Flare while the SIS will send a signal to the well choke valves and the gas lift valve to step down production so inlet separator flaring is no longer required.

# 5 Depressurization

During some shutdowns, it may be required to depressurize the equipment, system, or entire facility. The intent of depressurization is to relieve stress on the system by reducing the pressure, as well as safety deinventorying the system in order to reduce the impact of a leak, fire, or other emergency. The depressurization is enabled by blowdown valves that will actuate open to release the contained volume to the flare for all hydrocarbon gas systems. For most compressors, some degree of automated blowdown will be required to handle settle out pressure and protect integrity of gas seals. For process vessels, automated blowdown may not be required, rather would be a result of an Operator input. There could be certain process conditions that would drive an automated blowdown of certain process vessels or systems and this should be determined as part of the HAZOP/LOPA studies. This depressurization system is described in more detail in document Industry Source 03 Doc PRPHL-000001 *Relief and Blowdown Philosophy*.

# 6 Attachments

- Safety Instrumented System Hierarchy
