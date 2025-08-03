### ILayeredTooltipTextProvider API Reference

> Interface for custom tooltip text resolution.

#### Interface Declaration

```cpp
UINTERFACE(MinimalAPI)
class ULayeredTooltipTextProvider : public UInterface
{
    GENERATED_BODY()
};

class LAYEREDTOOLTIP_API ILayeredTooltipTextProvider
{
    GENERATED_BODY()
public:
    UFUNCTION(BlueprintNativeEvent, Category = "LayeredTooltip")
    void InitializeTextProvider();
    virtual void InitializeTextProvider_Implementation() {}

    UFUNCTION(BlueprintNativeEvent, Category = "LayeredTooltip")
    FText ResolveText(const FLayeredToolTipTriggerData& TriggerData);
    virtual FText ResolveText_Implementation(const FLayeredToolTipTriggerData& TriggerData)
    {
        return FText::GetEmpty();
    }
};
```

#### Functions

##### InitializeTextProvider

```cpp
UFUNCTION(BlueprintNativeEvent, Category = "LayeredTooltip")
void InitializeTextProvider();
virtual void InitializeTextProvider_Implementation() {}
```

- **Called:** Once during system startup
- **Default:** Empty implementation

##### ResolveText

```cpp
UFUNCTION(BlueprintNativeEvent, Category = "LayeredTooltip")
FText ResolveText(const FLayeredToolTipTriggerData& TriggerData);
virtual FText ResolveText_Implementation(const FLayeredToolTipTriggerData& TriggerData)
{
    return FText::GetEmpty();
}
```

- **Called:** Every time tooltip is displayed
- **Parameters:** `TriggerData` - Trigger configuration data
- **Returns:** Resolved text for display
- **Default:** Returns empty text

#### Implementation Notes

- **Blueprint Support:** Can be implemented in Blueprint or C++
- **BlueprintNativeEvent:** Functions use BlueprintNativeEvent pattern
- **Registration:** Set class in `Project Settings → LayeredTooltip Settings → Tooltip Text Provider Class`