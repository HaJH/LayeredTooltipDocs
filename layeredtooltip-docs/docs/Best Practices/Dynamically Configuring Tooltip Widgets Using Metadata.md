---
sidebar_position: 2
---
#### Dynamically Configuring Tooltip Widgets Using Metadata

> Use metadata to display various content types with a single tooltip widget.

![Dynamically Configuring -20250803111537472.webp](/assets/Dynamically%20Configuring%20Tooltip%20Widgets%20Using%20Metadata/Dynamically%20Configuring%20-20250803111537472.webp)

##### Registering Custom Widget Classes

Change the widget class in plugin settings.

![Dynamically Configuring Tooltip Widgets Using Metadata_1.webp](/assets/Dynamically%20Configuring%20Tooltip%20Widgets%20Using%20Metadata/Dynamically%20Configuring%20Tooltip%20Widgets%20Using%20Metadata_1.webp)

##### Dynamic Registration

**Metadata Configuration**

![Dynamically Configuring -20250803111537492.webp](/assets/Dynamically%20Configuring%20Tooltip%20Widgets%20Using%20Metadata/Dynamically%20Configuring%20-20250803111537492.webp)

**Metadata-Based Styling in Tooltip Widgets**

![Dynamically Configuring -20250803111537513.webp](/assets/Dynamically%20Configuring%20Tooltip%20Widgets%20Using%20Metadata/Dynamically%20Configuring%20-20250803111537513.webp)

##### Code Examples

**Setting Metadata:**

```cpp
void UInventorySlot::SetItem(UItemData* Item)
{
    FLayeredToolTipTriggerData TriggerData;
    TriggerData.TooltipData.Add("Type", "Item");
    TriggerData.TooltipData.Add("ItemId", Item->GetItemId());
    TriggerData.TooltipData.Add("Rarity", Item->GetRarityString());
    TriggerData.TriggerPayload = Item;
    
    ULayeredTooltipFunctionLibrary::RegisterWidgetAsTooltipTrigger(this, TriggerData);
}
```

**Type-Based Processing in Tooltip Widgets:**

```cpp
void UMyTooltipWidget::InitializeLayeredTooltip_Implementation(const FLayeredToolTipTriggerData& TriggerData)
{
    FString Type = TriggerData.TooltipData.FindRef("Type");
    
    if (Type == "Item")
    {
        ConfigureItemLayout(TriggerData);
    }
    else if (Type == "Skill")
    {
        ConfigureSkillLayout(TriggerData);
    }
}
```

**Conditional Styling:**

```cpp
void UMyTooltipWidget::ConfigureItemLayout(const FLayeredToolTipTriggerData& TriggerData)
{
    // Rarity-based coloring
    FString Rarity = TriggerData.TooltipData.FindRef("Rarity");
    FLinearColor Color = GetRarityColor(Rarity);
    BorderImage->SetColorAndOpacity(Color);
    
    // Level-based additional information
    FString Level = TriggerData.TooltipData.FindRef("Level");
    if (FCString::Atoi(*Level) >= 5)
    {
        AdvancedPanel->SetVisibility(ESlateVisibility::Visible);
    }
}
```