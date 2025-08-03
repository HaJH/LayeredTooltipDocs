#### Custom Tooltip Object

> You can create custom tooltip trigger logic by implementing the `ILayeredTooltipObject` interface.

#### Restrictions

**Important:** The `ILayeredTooltipObject` interface is currently **C++ only**.

- Cannot be implemented in Blueprints
- For Blueprint-only projects, refer to `ULayeredTooltipDefaultComponent`

#### Implementing the Interface

**Required Functions:**

```cpp
UCLASS()
class AMyCustomActor : public AActor, public ILayeredTooltipObject
{
    GENERATED_BODY()
public:
    // Required implementation
    virtual bool ShouldObjectTriggerTooltip() const override;
    virtual bool OverrideTooltipPositionInViewport(FVector2D& OutPosition) override;
    virtual FLayeredTooltipObjectDelegate& GetTooltipCloseDelegate() override;
    
    // Optional implementation
    virtual bool IsTriggerObjectVisible() const override;
    virtual void OnObjectTooltipOpened() override;
    virtual void OnObjectTooltipClosed() override;
    virtual void OnObjectTooltipPinned() override;
    
private:
    FLayeredTooltipObjectDelegate TooltipCloseDelegate;
};
```

**Component Implementation:**

```cpp
UCLASS(BlueprintSpawnableComponent)
class UMyTooltipComponent : public UActorComponent, public ILayeredTooltipObject
{
    GENERATED_BODY()
public:
    virtual bool ShouldObjectTriggerTooltip() const override;
    virtual FLayeredTooltipObjectDelegate& GetTooltipCloseDelegate() override;
    virtual bool OverrideTooltipPositionInViewport(FVector2D& OutPosition) override;
    
private:
    FLayeredTooltipObjectDelegate TooltipCloseDelegate;
};
```

#### Registering with the Tooltip System

```cpp
void AMyCustomActor::BeginPlay()
{
    Super::BeginPlay();
    
    FLayeredToolTipTriggerData TriggerData;
    TriggerData.TooltipData.Add("Type", "Actor");
    TriggerData.TriggerPayload = this;
    
    ULayeredTooltipFunctionLibrary::RegisterObjectAsTooltipTrigger(this, TriggerData);
}

void AMyCustomActor::EndPlay(const EEndPlayReason::Type EndPlayReason)
{
    ULayeredTooltipFunctionLibrary::UnregisterTooltipTriggerByObject(this);
    Super::EndPlay(EndPlayReason);
}
```

#### Core Function Descriptions

**ShouldObjectTriggerTooltip()**

- Core function that determines whether to display a tooltip
- May be called every frame, so performance considerations are necessary

```cpp
virtual bool ShouldObjectTriggerTooltip() const override
{
    // Implement custom trigger conditions
    return bIsInteractable && IsPlayerNearby();
}
```

**OverrideTooltipPositionInViewport()**

- Customize tooltip position
- Return `false` to use default cursor position

```cpp
virtual bool OverrideTooltipPositionInViewport(FVector2D& OutPosition) override
{
    // Calculate custom position
    if (CalculateCustomPosition(OutPosition))
    {
        return true; // Use custom position
    }
    return false; // Use default position
}
```

**GetTooltipCloseDelegate()**

- Provides a delegate to force-close tooltips from outside the plugin
- Must be returned by reference

```cpp
virtual FLayeredTooltipObjectDelegate& GetTooltipCloseDelegate() override
{
    return TooltipCloseDelegate;
}
```

#### Lifecycle Events

```cpp
virtual void OnObjectTooltipOpened() override
{
    // Logic when tooltip is displayed (e.g., highlight effect)
}

virtual void OnObjectTooltipClosed() override
{
    // Cleanup when tooltip is closed
}

virtual void OnObjectTooltipPinned() override
{
    // Enable additional functionality when tooltip is pinned
}
```

#### Reference: ULayeredTooltipDefaultComponent

Default component included with the plugin:

- Automatically detects the actor's first collision component
- Handles mouse over events automatically
- Suitable for simple actor tooltips

#### Important Notes

- Interface is currently C++ only (cannot be implemented in Blueprints)
- Performance optimization of `ShouldObjectTriggerTooltip()` is required
- Must unregister when actor is destroyed
- Delegate must be returned by reference