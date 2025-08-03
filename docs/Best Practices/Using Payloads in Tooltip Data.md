---
sidebar_position: 3
---
#### Using Payloads in Tooltip Data

> Use `TriggerPayload` to pass complex object data to tooltips.

##### Basic Usage

**Setting Payload:**

```cpp
void UInventorySlot::SetItem(UItemData* Item)
{
    FLayeredToolTipTriggerData TriggerData;
    TriggerData.TriggerPayload = Item;  // Pass object as payload
    
    ULayeredTooltipFunctionLibrary::RegisterWidgetAsTooltipTrigger(this, TriggerData);
}
```

**Using Payload in Tooltips:**

```cpp
void UItemTooltip::InitializeLayeredTooltip_Implementation(const FLayeredToolTipTriggerData& TriggerData)
{
    if (UItemData* Item = Cast<UItemData>(TriggerData.TriggerPayload))
    {
        SetItemIcon(Item->GetIcon());
        SetItemStats(Item->GetStats());
        SetItemDescription(Item->GetDescription());
    }
}
```

##### Real-Time Data Reflection

**Displaying Dynamic Information:**

```cpp
void UCharacterTooltip::InitializeLayeredTooltip_Implementation(const FLayeredToolTipTriggerData& TriggerData)
{
    if (AMyCharacter* Character = Cast<AMyCharacter>(TriggerData.TriggerPayload))
    {
        SetHealthBar(Character->GetHealthPercent());
        SetLevel(Character->GetLevel());
        SetActiveEffects(Character->GetActiveEffects());
    }
}
```

**Updating in Pinned State:**

```cpp
void UDynamicTooltip::OnLayeredTooltipPinned_Implementation(bool bPinned)
{
    if (bPinned)
    {
        GetWorld()->GetTimerManager().SetTimer(UpdateTimer, this, 
            &UDynamicTooltip::UpdateContent, 0.5f, true);
    }
    else
    {
        GetWorld()->GetTimerManager().ClearTimer(UpdateTimer);
    }
}
```

##### Usage in Text Providers

**Object-Based Text Generation:**

```cpp
FText UDynamicTextProvider::ResolveText_Implementation(const FLayeredToolTipTriggerData& TriggerData)
{
    if (UItemData* Item = Cast<UItemData>(TriggerData.TriggerPayload))
    {
        return FText::FromString(FString::Printf(TEXT("%s\nLevel: %d\nValue: %d gold"), 
            *Item->GetName(), Item->GetLevel(), Item->GetValue()));
    }
    
    return TriggerData.TooltipText;
}
```

##### Safe Usage

**Caching with Weak References:**

```cpp
class UTooltipWidget : public ULayeredTooltipUserWidget
{
private:
    TWeakObjectPtr<UObject> CachedPayload;
    
public:
    virtual void InitializeLayeredTooltip_Implementation(const FLayeredToolTipTriggerData& TriggerData) override
    {
        CachedPayload = TriggerData.TriggerPayload;
        if (CachedPayload.IsValid())
        {
            ProcessPayload(CachedPayload.Get());
        }
    }
    
    void UpdateContent()
    {
        if (CachedPayload.IsValid())
        {
            ProcessPayload(CachedPayload.Get());
        }
    }
};
```