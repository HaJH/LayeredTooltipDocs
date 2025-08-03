---
sidebar_position: 8
---
> Common issues and solutions for the LayeredTooltip system.

#### Tooltips Not Displaying

**Widget Registration Issues:**

- Ensure widget was **registered after being added to layout**
- Check registration status with `IsRegisteredAsTooltipTrigger`
- Verify trigger areas in debug mode

**System State Issues:**

- Check system activation status with `AreLayeredTooltipsEnabled()`
- Verify other UI elements aren't intercepting mouse events

**Configuration Issues:**

- Check if `TooltipDisplayDelay` value is too large
- Verify widget is actually visible on screen

#### Nested Tooltips Not Working

**Missing Decorator:**

- Verify `LayeredTooltipDecorator` is added to RichTextBlock
- Consider using `LayeredTooltipRichTextBlock`

#### Performance Issues

**Excessive Trigger Registration:**

- Check number of registered triggers in debug mode
- Unregister unnecessary triggers
- Utilize `bTransient` flag

**Memory Leaks:**

- Verify `UnregisterTooltipTriggerByWidget` is called when widget is destroyed
- Confirm registration is cleared in actor EndPlay

#### Custom Implementation Issues

**Text Provider:**

- Verify `InitializeTextProvider` is called
- Check for performance issues in `ResolveText` (called frequently)
- Confirm class is correctly set in plugin settings

**Tooltip Widget:**

- Verify `ILayeredTooltipWidget` interface implementation
- Confirm `GetOnTooltipDestroyDelegate()` implementation
- Check widget class is set in plugin settings

**Tooltip Object (C++ Only):**

- Verify `ILayeredTooltipObject` interface implementation
- Optimize `ShouldObjectTriggerTooltip()` performance
- Confirm delegate reference return

#### Editor-Related Issues

**Settings Application:**

- Some settings require editor restart
- Check project settings file (`DefaultGame.ini`)

**Plugin Activation:**

- Verify plugin activation status in `Edit → Plugins`
- Check engine version compatibility (UE 5.5 or higher)

#### Packaging-Related Issues

**Asset Inclusion:**

- Verify plugin content is included in packaging
- Confirm custom widget/text provider classes are included

**Debug Mode:**

- Disable debug mode in packaged builds

#### Additional Help

If issues persist:

- Compare with sample code in plugin documentation
- Use community forums or support channels