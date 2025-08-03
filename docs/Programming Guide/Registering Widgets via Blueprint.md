---
sidebar_position: 1
---
#### Registering Widgets via Blueprint

> Register widgets with the tooltip system through Blueprints without modifying widget design, or register dynamic widgets for runtime tooltip management.

##### Basic Usage

1. **Widget Registration**
   
    ![Register any widgets via blueprint-20250801134338804.webp](/assets/Registering%20Widgets%20via%20Blueprint/Register%20any%20widgets%20via%20blueprint-20250801134338804.webp)
    
    - Use the `RegisterWidgetAsTooltipTrigger` function to register widgets.
    - Register specific widgets within a widget Blueprint, or register the widget itself using a Self reference.
    - Widgets must be added to the layout before registration.
2. **Unregistration**
    
    - Use `UnregisterTooltipTriggerByWidget` to unregister widgets when no longer needed.

##### Lifecycle Management

**Persistent Registration**

- Registering with `bTransient = false` (default) maintains registration until explicitly unregistered.
- Requires manual unregistration.

**Transient Registration**

- Generally not required for typical use cases.
- Registering with `bTransient = true` creates volatile triggers that are automatically removed when tooltip stack levels change.
- Primarily used for temporary elements within nested tooltips.

##### Checking Registration Status

![Register any widgets via blueprint-20250801223809156.webp](/assets/Registering%20Widgets%20via%20Blueprint/Register%20any%20widgets%20via%20blueprint-20250801223809156.webp)

```cpp
bool bIsRegistered = ULayeredTooltipFunctionLibrary::IsRegisteredAsTooltipTrigger(MyWidget);
```

##### Related Functions

```cpp
// Widget registration/unregistration
static void RegisterWidgetAsTooltipTrigger(UWidget* InWidget, const FLayeredToolTipTriggerData& TooltipTriggerData, bool bTransient = false);
static void UnregisterTooltipTriggerByWidget(UWidget* Widget);

// Check registration status
static bool IsRegisteredAsTooltipTrigger(UObject* InObject);
```

##### Important Notes

- `bTransient = true` is for one-time tooltips that are automatically removed when tooltip hierarchy changes.
- Persistently registered widgets must be manually unregistered to prevent memory leaks.
- The tooltip system automatically detects widget visibility changes.