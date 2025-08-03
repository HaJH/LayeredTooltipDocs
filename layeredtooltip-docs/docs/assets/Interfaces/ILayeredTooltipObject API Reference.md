### ILayeredTooltipObject API Reference

> Interface for UObject tooltip trigger implementation.

#### Interface Declaration

```cpp
UINTERFACE(MinimalAPI, meta = (CannotImplementInterfaceInBlueprint))
class ULayeredTooltipObject : public UInterface
{
    GENERATED_BODY()
};

class LAYEREDTOOLTIP_API ILayeredTooltipObject
{
    GENERATED_BODY()
public:
    virtual bool IsTriggerObjectVisible() const { return true; }
    virtual bool ShouldObjectTriggerTooltip() const = 0;
    virtual void OnObjectTooltipPinned() {}
    virtual void OnObjectTooltipClosed() {}
    virtual void OnObjectTooltipOpened() {}
    virtual bool OverrideTooltipPositionInViewport(FVector2D& OutPosition) = 0;
    virtual FLayeredTooltipObjectDelegate& GetTooltipCloseDelegate() = 0;
};
```

#### Functions

##### IsTriggerObjectVisible

```cpp
virtual bool IsTriggerObjectVisible() const { return true; }
```

- **Returns:** True if object should participate in tooltip logic
- **Default:** Returns `true`

##### ShouldObjectTriggerTooltip

```cpp
virtual bool ShouldObjectTriggerTooltip() const = 0;
```

- **Purpose:** Primary gate for tooltip activation
- **Returns:** True if tooltip should be triggered
- **Note:** Pure virtual function

##### OnObjectTooltipPinned

```cpp
virtual void OnObjectTooltipPinned() {}
```

- **Called:** When tooltip is pinned
- **Default:** Empty implementation

##### OnObjectTooltipClosed

```cpp
virtual void OnObjectTooltipClosed() {}
```

- **Called:** When tooltip is closed
- **Default:** Empty implementation

##### OnObjectTooltipOpened

```cpp
virtual void OnObjectTooltipOpened() {}
```

- **Called:** When tooltip becomes visible
- **Default:** Empty implementation

##### OverrideTooltipPositionInViewport

```cpp
virtual bool OverrideTooltipPositionInViewport(FVector2D& OutPosition) = 0;
```

- **Parameters:** `OutPosition` - [Out] Screen position for tooltip
- **Returns:** True to use custom position, false for default
- **Note:** Pure virtual function

##### GetTooltipCloseDelegate

```cpp
virtual FLayeredTooltipObjectDelegate& GetTooltipCloseDelegate() = 0;
```

- **Returns:** Reference to delegate for external tooltip closure requests
- **Note:** Pure virtual function

#### Delegate Type

```cpp
DECLARE_DELEGATE_OneParam(FLayeredTooltipObjectDelegate, UObject*);
```

#### Implementation Notes

- **Blueprint Support:** Cannot be implemented in Blueprints (CannotImplementInterfaceInBlueprint)
- **Pure Virtual Functions:** `ShouldObjectTriggerTooltip`, `OverrideTooltipPositionInViewport`, `GetTooltipCloseDelegate`
- **Registration Required:** Must use `ULayeredTooltipFunctionLibrary::RegisterObjectAsTooltipTrigger`