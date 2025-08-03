#### Auto-Adding Rich Text Decorators via Widget Base Classes

> Use base classes to automatically enable nested tooltips in all project widgets.

##### Method 1: Using the Provided Base Class

Change the widget Blueprint's parent class to `LayeredTooltipEnabledUserWidget` to automatically add decorators to all RichTextBlocks.

##### Method 2: Custom Base Class

```cpp
void UMyBaseWidget::NativeConstruct()
{
    Super::NativeConstruct();
    
    TArray<UWidget*> AllWidgets;
    WidgetTree->GetAllWidgets(AllWidgets);
    
    for (UWidget* Widget : AllWidgets)
    {
        if (URichTextBlock* RichTextBlock = Cast<URichTextBlock>(Widget))
        {
            RichTextBlock->SetDecorators({ULayeredTooltipDecorator::StaticClass()});
        }
    }
}
```

##### Using Individual RichTextBlocks

`LayeredTooltipRichTextBlock` automatically includes the decorator.

##### Important Notes

Exercise caution when using existing decorators, as `SetDecorators` will overwrite them.