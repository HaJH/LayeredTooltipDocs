---
sidebar_position: 2
---
#### Registering Any Object with the Tooltip System

![Registering Any Object with the Tooltip System.webp](/assets/Registering%20Actors%20with%20the%20Tooltip%20System%20Using%20Dedicated%20Components/Registering%20Any%20Object%20with%20the%20Tooltip%20System.webp)

> Register any object implementing the ILayeredTooltipObject interface with the tooltip system. Reference `ULayeredTooltipDefaultComponent` for implementation guidance.

##### Basic Usage

1. **Object Registration**
    
    - Register UObjects with the tooltip system using the `RegisterObjectAsTooltipTrigger` function.
    - Registered objects control tooltip display through the `ILayeredTooltipObject` interface.
2. **Interface Implementation Constraints**
    
    - **Important**: The `ILayeredTooltipObject` interface currently cannot be implemented in Blueprints.
    - Native C++ implementation only.
    - For Blueprint-only projects, use `ULayeredTooltipDefaultComponent`.
3. **Unregistration**
    
    - Use `UnregisterTooltipTriggerByObject` to unregister objects.

##### Related Functions

```cpp
// Object registration/unregistration
static void RegisterObjectAsTooltipTrigger(UObject* InObject, const FLayeredToolTipTriggerData& TooltipTriggerData, bool bTransient = false);
static void UnregisterTooltipTriggerByObject(UObject* InObject);

// Check registration status
static bool IsRegisteredAsTooltipTrigger(UObject* InObject);

// Modify tooltip settings
static void SetTooltipTriggerDisplayDelay(UObject* InTriggerObject, float Delay);
static void SetTooltipTriggerOffset(UObject* InTriggerObject, const FVector2D& InOffset);

// Query tooltip status
static UUserWidget* GetLayeredTooltipWidget(const UObject* InTriggerObject);
static bool IsTooltipPinned(const UObject* TriggerObject);
```

##### Important Notes

- The `ILayeredTooltipObject` interface currently cannot be implemented in Blueprints (native C++ only).
- Recommended to call `UnregisterTooltipTriggerByObject` before object destruction to prevent memory leaks.
- Unlike widgets, objects cannot automatically detect mouse-over events, requiring interface implementation or manual triggering.

##### Reference: ULayeredTooltipDefaultComponent

![Registering Any Object with the Tooltip System.webp](/assets/Registering%20Actors%20with%20the%20Tooltip%20System%20Using%20Dedicated%20Components/Registering%20Any%20Object%20with%20the%20Tooltip%20System.webp) 

A sample component included with the plugin that provides basic Actor tooltip functionality:

- Automatically connects to the Actor's first collision-enabled component
- Handles mouse-over events and tooltip lifecycle management
- Reference implementation for simple Actor tooltip requirements