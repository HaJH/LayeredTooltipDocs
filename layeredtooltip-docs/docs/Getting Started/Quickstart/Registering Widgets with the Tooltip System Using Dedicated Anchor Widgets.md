---
sidebar_position: 2
---
> Register any widget with the tooltip system using `LayeredTooltipBorderAnchor` and `LayeredTooltipAutoAnchor`.

1. Select the widget you want to register with the tooltip system. 
   ![[Registering Widgets -20250803111258694.webp]]
    
2. In the Widget Designer hierarchy, wrap the widget using `Wrap With... → Layered Tooltip Border Anchor`. 
   ![[Registering Widgets -20250803111258730.webp]]
    
    ![[Registering Widgets -20250803111258797.webp]]
    
3. Select the created `LayeredTooltipBorderAnchor`.
    
4. Configure tooltip data for the widget in the Details tab. 
   ![[Registering Widgets -20250803111258822.webp]]
    
    1. Enter tooltip text directly for simple cases. 
       ![[Registering Widgets -20250803111258882.webp]]
    2. Alternatively, configure metadata to retrieve tooltip text through `LayeredTooltipTextProvider`. The default implementation looks up TextId in the String Table. 
       ![[Registering Widgets -20250803111258895.webp]]
5. Child widgets registered via `LayeredTooltipBorderAnchor` have mouse-over detection and lifecycle management handled automatically. 
   ![[Registering Widgets -20250803111258953.webp]]
    
6. Use `LayeredTooltipAutoAnchor` to register child widgets, parent panel widgets, or the widget Blueprint itself with the tooltip system.
    
    ![[Registering Widgets -20250803111258979.webp]]
    
    ![[Registering Widgets -20250803111259008.webp]]
    
    ![[Registering Widgets -20250803111259052.webp]]
    
7. The child widget wrapped with `LayeredTooltipBorderAnchor` is now registered with the tooltip system. 
   ![[Registering Widgets -20250803111259106.webp]]
