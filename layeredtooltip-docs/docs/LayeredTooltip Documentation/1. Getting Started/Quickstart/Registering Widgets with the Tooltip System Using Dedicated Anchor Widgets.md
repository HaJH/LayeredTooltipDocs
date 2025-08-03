#### Registering Widgets with the Tooltip System Using Dedicated Anchor Widgets

> Register any widget with the tooltip system using `LayeredTooltipBorderAnchor` and `LayeredTooltipAutoAnchor`.

1. Select the widget you want to register with the tooltip system. 
   ![[docs/LayeredTooltip Documentation/1. Getting Started/Quickstart/Registering Widgets with the Tooltip System Using Dedicated Anchor Widgets/Registering Widgets -20250803111258694.webp|LayeredTooltip Documentation/LayeredTooltip Documentation-18.webp]]
    
2. In the Widget Designer hierarchy, wrap the widget using `Wrap With... → Layered Tooltip Border Anchor`. 
   ![[docs/LayeredTooltip Documentation/1. Getting Started/Quickstart/Registering Widgets with the Tooltip System Using Dedicated Anchor Widgets/Registering Widgets -20250803111258730.webp|LayeredTooltip Documentation/LayeredTooltip Documentation-19.webp]]
    
    ![[docs/LayeredTooltip Documentation/1. Getting Started/Quickstart/Registering Widgets with the Tooltip System Using Dedicated Anchor Widgets/Registering Widgets -20250803111258797.webp|LayeredTooltip Documentation/LayeredTooltip Documentation-20.webp]]
    
3. Select the created `LayeredTooltipBorderAnchor`.
    
4. Configure tooltip data for the widget in the Details tab. 
   ![[docs/LayeredTooltip Documentation/1. Getting Started/Quickstart/Registering Widgets with the Tooltip System Using Dedicated Anchor Widgets/Registering Widgets -20250803111258822.webp|LayeredTooltip Documentation/LayeredTooltip Documentation-21.webp]]
    
    1. Enter tooltip text directly for simple cases. 
       ![[docs/LayeredTooltip Documentation/1. Getting Started/Quickstart/Registering Widgets with the Tooltip System Using Dedicated Anchor Widgets/Registering Widgets -20250803111258882.webp|LayeredTooltip Documentation/LayeredTooltip Documentation-22.webp]]
    2. Alternatively, configure metadata to retrieve tooltip text through `LayeredTooltipTextProvider`. The default implementation looks up TextId in the String Table. 
       ![[docs/LayeredTooltip Documentation/1. Getting Started/Quickstart/Registering Widgets with the Tooltip System Using Dedicated Anchor Widgets/Registering Widgets -20250803111258895.webp|LayeredTooltip Documentation/LayeredTooltip Documentation-23.webp]]
5. Child widgets registered via `LayeredTooltipBorderAnchor` have mouse-over detection and lifecycle management handled automatically. 
   ![[docs/LayeredTooltip Documentation/1. Getting Started/Quickstart/Registering Widgets with the Tooltip System Using Dedicated Anchor Widgets/Registering Widgets -20250803111258953.webp|LayeredTooltip Documentation/LayeredTooltip Documentation-24.webp]]
    
6. Use `LayeredTooltipAutoAnchor` to register child widgets, parent panel widgets, or the widget Blueprint itself with the tooltip system.
    
    ![[docs/LayeredTooltip Documentation/1. Getting Started/Quickstart/Registering Widgets with the Tooltip System Using Dedicated Anchor Widgets/Registering Widgets -20250803111258979.webp|LayeredTooltip Documentation/LayeredTooltip Documentation-25.webp]]
    
    ![[docs/LayeredTooltip Documentation/1. Getting Started/Quickstart/Registering Widgets with the Tooltip System Using Dedicated Anchor Widgets/Registering Widgets -20250803111259008.webp|LayeredTooltip Documentation/LayeredTooltip Documentation-26.webp]]
    
    ![[docs/LayeredTooltip Documentation/1. Getting Started/Quickstart/Registering Widgets with the Tooltip System Using Dedicated Anchor Widgets/Registering Widgets -20250803111259052.webp|LayeredTooltip Documentation/LayeredTooltip Documentation-27.webp]]
    
7. The child widget wrapped with `LayeredTooltipBorderAnchor` is now registered with the tooltip system. 
   ![[docs/LayeredTooltip Documentation/1. Getting Started/Quickstart/Registering Widgets with the Tooltip System Using Dedicated Anchor Widgets/Registering Widgets -20250803111259106.webp|LayeredTooltip Documentation/LayeredTooltip Documentation-28.webp]]

![[Registering Widgets with the Tooltip System Using Dedicated Anchor Widgets/Registering Widgets -20250803111133983.webp]]