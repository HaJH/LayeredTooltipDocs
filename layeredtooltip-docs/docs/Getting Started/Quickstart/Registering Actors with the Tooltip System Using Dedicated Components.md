---
sidebar_position: 3
---
#### Registering Actors with the Tooltip System Using Dedicated Components

> Add tooltip functionality to Actors without code using the `LayeredTooltipDefaultComponent`.  
> **Note:** This component serves as a sample/reference implementation and may not satisfy all requirements for production game projects. For greater control, extend the implementation using C++ or Blueprints directly.

1. Create an Actor. 
   ![[Registering Actors with -20250803111344005.webp|LayeredTooltip Documentation/LayeredTooltip Documentation-20250731001112175.webp]]
    
2. Add any `PrimitiveComponent`. A Cube is used in this example.
    
3. Ensure collision is enabled for the `PrimitiveComponent`. Collision Query must be enabled for mouse-over detection. ![[Registering Actors with -20250803111344024.webp|LayeredTooltip Documentation/LayeredTooltip Documentation-20250731002205808.webp]]
    
4. Add `LayeredTooltipDefaultComponent` to the Actor. ![[Registering Actors with -20250803111344086.webp|LayeredTooltip Documentation/LayeredTooltip Documentation-20250731002427509.webp]]
    
    > This component automatically finds the Actor's first collision-enabled `PrimitiveComponent` and handles mouse-over events.
    
5. Select the component and configure tooltip information in the Details tab. ![[Registering Actors with -20250803111344163.webp|LayeredTooltip Documentation/LayeredTooltip Documentation-20250731002612711.webp]]
    
6. To use this functionality, the `PlayerController` must have `bEnableMouseOverEvents` enabled. 
   ![[Registering Actors with -20250803111344181.webp|LayeredTooltip Documentation/LayeredTooltip Documentation-20250731002724536.webp]]
    
7. The Actor now displays tooltips. Use the `bOverrideTooltipPositionInViewport` flag to control tooltip positioning. 
   ![[docs/assets/Registering Actors with the Tooltip System Using Dedicated Components/Registering Any Object with the Tooltip System.webp|LayeredTooltip Documentation/LayeredTooltip Documentation-20250731013925873.webp]]