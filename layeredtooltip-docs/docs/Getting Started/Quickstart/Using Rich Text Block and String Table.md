---
sidebar_position: 1
---
> Using Rich Text Block and String Table

1. **Add Rich Text Block**
    
    1. Add a RichTextBlock in the Widget Designer. 
       
       ![[RichTextBlock.webp]]
        
        > Alternatively, use LayeredTooltipRichTextBlock to skip steps 2 and 3.
        
    2. In the Details tab of the added RichTextBlock, locate Decorator Classes. 
    
    ![[RichTextBlock-1.webp]]
    
    3. Add LayeredTooltipDecorator. 
    
    ![[RichTextBlock-2.webp]]
    
    4. Assign an appropriate TextStyleSet to the RichTextBlock. 
    
    ![[RichTextBlock-3.webp]]
    
        
        > We'll use the pre-configured DT_LayeredTooltip_Default_RichText for this example. Tag configuration for tooltips will be covered below.
        
2. **Writing Text**
    
    1. Add the `<Tooltip>` tag to your text. 
       
    ![[RichTextBlock-4.webp]]
    
    2. Now hovering over the tagged word will display a tooltip. 
       
    ![[RichTextBlock-5.webp]]
    
3. **Preparing Tooltip Content**
    
    > Implement LayeredTooltipTextProvider for complete control over tooltip content display. The default LayeredTooltipDefaultTextProvider uses String Tables to define tooltip content.
    
    1. Modify the default String Table in Plugin Content. Open `ST_LayeredTooltip_Default` at `Plugins/LayeredTooltip/DefaultResources/`. 
       
    ![[RichTextBlock-6.webp]]
    
    2. Create a string key named `tooltip_plugin`. 
       
    ![[RichTextBlock-7.webp]]
    
    3. Add the string key to the text. Change from `<Tooltip>` to `<Tooltip TextId="tooltip_plugin">` to include the TextId. 
       
    ![[RichTextBlock-8.webp]]
        
        > Tags like `Tooltip` and `TextId` can be customized through `Plugin Settings → Tooltip Tags, Tooltip Text Metadata Key`.
        
4. **Tooltip content is now displayed.** 
   
![[RichTextBlock-9.webp]]

    
5. **Implement nested tooltips by adding additional tags within tooltip content.** 
   
![[RichTextBlock-10.webp]] 

![[RichTextBlock-11.webp]]
    
> The above content is defined in the String Table as follows: 

```
LayeredTooltip Plugin. <tooltip textid="tooltip_plugin">This plugin</> allows you to freely link another <tooltip textid="tooltip_tooltip">tooltip</> to the text in the <tooltip textid="tooltip_tooltip">tooltip</>. Create as many nested tooltips as you want and stack them up.
```