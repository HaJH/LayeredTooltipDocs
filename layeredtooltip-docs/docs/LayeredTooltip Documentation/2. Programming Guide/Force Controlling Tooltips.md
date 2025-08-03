#### Force Controlling Tooltips

> Functions for immediately displaying or hiding tooltips, or directly controlling the tooltip system.

##### Force Tooltip Display

1. **Force Display and Pin Tooltips**
    
    ```cpp
    // Close all tooltips and force display the specified object's tooltip with pinning
    ULayeredTooltipFunctionLibrary::ForceShowAndPinTooltip(MyObject);
    ```
    
2. **Pin Tooltip**
    
    ```cpp
    // Pin the currently displayed tooltip (remains visible when mouse moves away)
    ULayeredTooltipFunctionLibrary::PinTooltip(MyObject);
    ```
    

##### Closing Tooltips

1. **Close All Tooltips**
    
    ```cpp
    // Close all tooltips (including pinned tooltips)
    ULayeredTooltipFunctionLibrary::CloseAllTooltips();
    ```
    

##### System Control

1. **Enable/Disable Tooltip System**
    
    ```cpp
    // Disable tooltip system (all tooltips close automatically)
    ULayeredTooltipFunctionLibrary::SetLayeredTooltipsEnable(false);
    
    // Re-enable
    ULayeredTooltipFunctionLibrary::SetLayeredTooltipsEnable(true);
    
    // Check activation status
    bool bEnabled = ULayeredTooltipFunctionLibrary::AreLayeredTooltipsEnabled();
    ```
    
2. **Status Queries**
    
    ```cpp
    // Check if any tooltips are currently displayed
    bool bAnyVisible = ULayeredTooltipFunctionLibrary::IsAnyLayeredTooltipVisible();
    
    // Check if mouse is over any tooltip
    bool bMouseOverTooltip = ULayeredTooltipFunctionLibrary::IsMouseOverAnyTooltip();
    ```
    

##### Use Cases

- **Tutorials**: Force display tooltips at specific steps
- **Game Pause**: Close all tooltips when game is paused
- **Modal UI**: Disable tooltip system when important UI opens
- **Debugging**: Test tooltip behavior during development

##### Related Functions

```cpp
// Force tooltip display
static void ForceShowAndPinTooltip(UObject* InTriggerObject);
static void PinTooltip(UObject* TriggerObject);

// Close tooltips
static void CloseAllTooltips();

// System control
static void SetLayeredTooltipsEnable(bool bEnabled);
static bool AreLayeredTooltipsEnabled();

// Status queries
static bool IsAnyLayeredTooltipVisible();
static bool IsMouseOverAnyTooltip();
```