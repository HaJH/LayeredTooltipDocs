### Custom Tooltip Widget

> You can create custom tooltip appearance and behavior by implementing the `ILayeredTooltipWidget` interface.

#### Implementing the Interface

**Blueprint Implementation:**

![[docs/LayeredTooltip Documentation/4. Advanced Usage/Custom Tooltip Widget/Custom Tooltip Widget-20250802145617328.webp]] ![[docs/LayeredTooltip Documentation/4. Advanced Usage/Custom Tooltip Widget/Custom Tooltip Widget-20250802145931001.webp]]

- Add the `ILayeredTooltipWidget` interface in `Class Settings → Interfaces → Implemented Interfaces`
- Implement each interface function in Blueprint

![[docs/LayeredTooltip Documentation/4. Advanced Usage/Custom Tooltip Widget/Custom Tooltip Widget-20250802145119869.webp]]

**C++ Implementation:**

```cpp
UCLASS()
class UMyCustomTooltipWidget : public UUserWidget, public ILayeredTooltipWidget
{
    GENERATED_BODY()
public:
    // Required implementation
    virtual void InitializeLayeredTooltip_Implementation(const FLayeredToolTipTriggerData& TriggerData) override;
    virtual void SetLayeredTooltipTitle_Implementation(const FText& InText) override;
    virtual void SetLayeredTooltipText_Implementation(const FText& InText) override;
    virtual FOnTooltipDestroyDelegate& GetOnTooltipDestroyDelegate() override;
    
    // Optional implementation
    virtual void OnLayeredTooltipPinned_Implementation(bool bPinned) override;
    virtual void OnLayeredTooltipStartTimer_Implementation(float Time) override;
    virtual void OnLayeredTooltipStopTimer_Implementation() override;

private:
    FOnTooltipDestroyDelegate OnTooltipDestroy;
};
```

#### Advanced Initialization

**Payload-Based Dynamic Configuration:**

```cpp
void UMyCustomTooltipWidget::InitializeLayeredTooltip_Implementation(const FLayeredToolTipTriggerData& TriggerData)
{
    // Change layout based on metadata
    FString Type = TriggerData.TooltipData.FindRef("Type");
    ConfigureLayoutForType(Type);
    
    // Process complex data through payload
    if (TriggerData.TriggerPayload)
    {
        ProcessPayloadData(TriggerData.TriggerPayload);
    }
}

void UMyCustomTooltipWidget::ProcessPayloadData(UObject* Payload)
{
    if (UItemData* Item = Cast<UItemData>(Payload))
    {
        // Display real-time item information
        UpdateItemStats(Item);
        BuildDynamicContent(Item);
    }
    else if (ACharacter* Character = Cast<ACharacter>(Payload))
    {
        // Monitor character status in real-time
        MonitorCharacterStats(Character);
    }
}
```

#### Pin State Management

**Interactive Element Control:**

```cpp
void UMyCustomTooltipWidget::OnLayeredTooltipPinned_Implementation(bool bPinned)
{
    if (bPinned)
    {
        // Advanced features shown only when pinned
        DetailedInfoPanel->SetVisibility(ESlateVisibility::Visible);
        InteractiveButtons->SetVisibility(ESlateVisibility::Visible);
        
        // Start real-time updates
        StartRealtimeUpdates();
    }
    else
    {
        StopRealtimeUpdates();
        DetailedInfoPanel->SetVisibility(ESlateVisibility::Hidden);
    }
}
```

**Custom Timer UI:**

```cpp
void UMyCustomTooltipWidget::OnLayeredTooltipStartTimer_Implementation(float Time)
{
    // Custom timer animation
    if (TimerWidget)
    {
        TimerWidget->StartCountdown(Time);
    }
    
    // Visual feedback
    PlayTimerStartEffect();
}
```

#### Nested Tooltip Support

**Dynamic Rich Text Configuration:**

```cpp
void UMyCustomTooltipWidget::NativeConstruct()
{
    Super::NativeConstruct();
    
    // Add decorators to all rich text blocks
    TArray<UWidget*> AllWidgets;
    WidgetTree->GetAllWidgets(AllWidgets);
    
    for (UWidget* Widget : AllWidgets)
    {
        if (URichTextBlock* RichText = Cast<URichTextBlock>(Widget))
        {
            RichText->SetDecorators({ULayeredTooltipDecorator::StaticClass()});
        }
    }
}
```

#### Register in Plugin Settings

![[docs/LayeredTooltip Documentation/3. Best Practices/Dynamically Configuring Tooltip Widgets Using Metadata/Dynamically Configuring Tooltip Widgets Using Metadata_1.webp]] Set your custom widget class in `Project Settings → Plugins → LayeredTooltip Settings → Layered Tooltip Widget Class`.