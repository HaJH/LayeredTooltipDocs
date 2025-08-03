---
sidebar_position: 3
---
#### Setting Priority Triggers

> Objects set as priority triggers always display tooltips regardless of mouse-over status. Use when you want to manually display specific tooltips.

##### Basic Usage

1. **Set Priority Trigger**
    
    ```cpp
    // Set object as priority trigger
    ULayeredTooltipFunctionLibrary::SetPriorityTrigger(MyObject);
    
    // Set by ID
    ULayeredTooltipFunctionLibrary::SetPriorityTriggerById(TriggerId);
    ```
    
2. **Clear Priority Trigger**
    
    ```cpp
    // Clear current priority trigger
    ULayeredTooltipFunctionLibrary::ClearPriorityTrigger();
    ```
    

##### Usage Scenarios

- **NPC Interaction**: Automatically display interaction tooltips when player is near NPCs
- **Item Inspection Mode**: Automatically display tooltips on items in specific modes
- **Quest Guide**: Automatically display guidance tooltips on quest target objects

##### Related Functions

```cpp
// Set/Clear priority triggers
static void SetPriorityTrigger(UObject* InTriggerObject);
static void SetPriorityTriggerById(const FString& InTriggerId);
static void ClearPriorityTrigger();
```

##### Important Notes

- Only one priority trigger can be set at a time.
- Objects must first be registered with `RegisterObjectAsTooltipTrigger` before setting as priority triggers.
- Call `ClearPriorityTrigger()` when no longer needed to release priority status.