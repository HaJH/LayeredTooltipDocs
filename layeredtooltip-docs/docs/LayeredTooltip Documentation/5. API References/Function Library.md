### Function Library

> `ULayeredTooltipFunctionLibrary` is a Blueprint function library that provides access to all tooltip system features.

#### Registration & Management

**RegisterWidgetAsTooltipTrigger**

```cpp
static void RegisterWidgetAsTooltipTrigger(UWidget* InWidget, const FLayeredToolTipTriggerData& TooltipTriggerData, bool bTransient = false);
```

- **Description:** Registers a widget as a tooltip trigger
- **Parameters:**
    - `InWidget`: Widget to register (must be added to layout)
    - `TooltipTriggerData`: Tooltip data and settings
    - `bTransient`: If true, creates a transient trigger (automatically removed when tooltip hierarchy changes)

**UnregisterTooltipTriggerByWidget**

```cpp
static void UnregisterTooltipTriggerByWidget(UWidget* InWidget);
```

- **Description:** Unregisters tooltip from widget
- **Purpose:** Prevents memory leaks when widget is destroyed

**RegisterObjectAsTooltipTrigger**

```cpp
static void RegisterObjectAsTooltipTrigger(UObject* InTriggerObject, const FLayeredToolTipTriggerData& TooltipTriggerData, bool bTransient = false);
```

- **Description:** Registers any UObject as a tooltip trigger
- **Purpose:** Adds tooltips to non-widget objects like actors and components
- **Requirements:** Must implement `ILayeredTooltipObject` interface (C++ only)

**UnregisterTooltipTriggerByObject**

```cpp
static void UnregisterTooltipTriggerByObject(UObject* InTriggerObject);
```

- **Description:** Unregisters tooltip from object

**IsRegisteredAsTooltipTrigger**

```cpp
static bool IsRegisteredAsTooltipTrigger(UObject* InObject);
```

- **Description:** Checks if object is registered as tooltip trigger
- **Return Value:** Registration status (true/false)

#### System Control

**SetLayeredTooltipsEnable**

```cpp
static void SetLayeredTooltipsEnable(bool bEnabled);
```

- **Description:** Enables/disables entire tooltip system
- **Purpose:** Hide all tooltips during cutscenes or special game modes

**AreLayeredTooltipsEnabled**

```cpp
static bool AreLayeredTooltipsEnabled();
```

- **Description:** Check tooltip system activation status

**CloseAllTooltips**

```cpp
static void CloseAllTooltips();
```

- **Description:** Close all currently displayed tooltips
- **Purpose:** Clean up tooltips when opening menus or dialogs

#### Configuration

**SetTooltipTriggerDisplayDelay**

```cpp
static void SetTooltipTriggerDisplayDelay(UObject* InTriggerObject, float Delay);
```

- **Description:** Set display delay time for specific trigger
- **Parameters:**
    - `Delay`: Delay time in seconds (0.0 for instant display)

**SetTooltipTriggerOffset**

```cpp
static void SetTooltipTriggerOffset(UObject* InTriggerObject, const FVector2D& InOffset);
```

- **Description:** Set position offset for specific trigger
- **Parameters:**
    - `InOffset`: Pixel offset (x: left/right, y: up/down)

#### Query Functions

**GetLayeredTooltipWidget**

```cpp
static UUserWidget* GetLayeredTooltipWidget(const UObject* InTriggerObject);
```

- **Description:** Returns tooltip widget associated with trigger object
- **Return Value:** Active tooltip widget or nullptr
- **Purpose:** Dynamic tooltip content modification, custom interactions

**IsAnyLayeredTooltipVisible**

```cpp
static bool IsAnyLayeredTooltipVisible();
```

- **Description:** Check if any tooltips are currently displayed
- **Purpose:** UI state management, game logic condition checking

**IsTooltipPinned**

```cpp
static bool IsTooltipPinned(const UObject* TriggerObject);
```

- **Description:** Check if specific trigger's tooltip is pinned

#### Display Control

**ForceShowAndPinTooltip**

```cpp
static void ForceShowAndPinTooltip(UObject* InTriggerObject);
```

- **Description:** Immediately display and pin tooltip
- **Purpose:** Tutorials, forcing display of important information
- **Behavior:** Close all existing tooltips → Display specified tooltip → Immediately pin

**PinTooltip**

```cpp
static void PinTooltip(UObject* TriggerObject);
```

- **Description:** Pin currently displayed tooltip
- **Effect:** Tooltip remains visible when mouse moves away, enables interactive elements

#### Priority System

**SetPriorityTrigger**

```cpp
static void SetPriorityTrigger(UObject* InTriggerObject);
```

- **Description:** Set specified trigger as priority trigger
- **Effect:** Always displays tooltip regardless of mouse hover
- **Purpose:** NPC interactions, quest guidance

**SetPriorityTriggerById**

```cpp
static void SetPriorityTriggerById(const FString& InTriggerId);
```

- **Description:** Set priority trigger by ID
- **Requirements:** Trigger must be registered first

**ClearPriorityTrigger**

```cpp
static void ClearPriorityTrigger();
```

- **Description:** Clear priority trigger
- **Effect:** Restore normal mouse hover behavior

#### Mouse Interaction

**IsMouseOverAnyTooltip**

```cpp
static bool IsMouseOverAnyTooltip();
```

- **Description:** Check if mouse is over any tooltip
- **Purpose:** Prevent tooltip closure when interacting with tooltip content

#### Positioning Utilities

**CalculateTooltipPositionAtCursor**

```cpp
static FVector2D CalculateTooltipPositionAtCursor(UWidget* Widget, FVector2D InOffset);
```

- **Description:** Calculate optimal tooltip position based on mouse cursor
- **Return Value:** Tooltip position considering screen boundaries (viewport coordinates)

**CalculateClampedTooltipPosition**

```cpp
static FVector2D CalculateClampedTooltipPosition(UWidget* Widget, FVector2D InOffset, FVector2D DesiredPosition);
```

- **Description:** Calculate tooltip position with screen boundary constraints
- **Parameters:**
    - `DesiredPosition`: Desired position (viewport coordinates)
- **Return Value:** Position adjusted within screen boundaries

**PositionTooltipWidgetAtCursor**

```cpp
static void PositionTooltipWidgetAtCursor(UUserWidget* UserWidget, FVector2D InOffset);
```

- **Description:** Position tooltip widget near mouse cursor
- **Behavior:** Calculate widget size → Calculate optimal position → Place in viewport

**PositionTooltipWidgetAtPosition**

```cpp
static void PositionTooltipWidgetAtPosition(UUserWidget* UserWidget, FVector2D InOffset, FVector2D DesiredPosition);
```

- **Description:** Position tooltip widget at specified screen coordinates
- **Purpose:** Actor-based tooltips, custom positioning

#### Settings Access

**GetLayeredTooltipSettings**

```cpp
static ULayeredTooltipSettings* GetLayeredTooltipSettings();
```

- **Description:** Return plugin settings instance
- **Purpose:** Read settings at runtime, dynamic configuration changes