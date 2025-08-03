---
sidebar_position: 7
---
### Debug Features

> You can analyze the tooltip system and resolve issues using the plugin's debug mode.

#### Enabling Debug Mode

**Enable in Plugin Settings:**

Check `Project Settings → Plugins → LayeredTooltip Settings → Layered Tooltip Debug`.

![5.Debug Features-20250802152905531.webp](/assets/Debug%20Features/5.Debug%20Features-20250802152905531.webp)

#### Debug Features

**Visual Debugging:**

- Highlight registered tooltip trigger areas
- Display tooltip trigger object information on screen
- Visualize active tooltip hierarchy structure

![5.Debug Features-20250802153011109.webp](/assets/Debug%20Features/5.Debug%20Features-20250802153011109.webp)

**Log Output:**

- Log tooltip registration/unregistration events
- Track trigger state changes
- Output metadata content

#### Checking Debug Information

**On-Screen Debug Information:** 

![5.Debug Features-20250802153218307.webp](/assets/Debug%20Features/5.Debug%20Features-20250802153218307.webp)

```
(Layered Tooltip Trigger - Widget Count: 5, Object Count: 3)
MyButton_Widget
ItemSlot_1
SkillButton_Fire
NPCInteraction_Guard
QuestGiver_Merchant
```

**Metadata Output:** When text ID is not found, raw metadata is displayed:

```
----Raw Metadata----
Type: Item
ItemId: sword_001
Rarity: epic
Category: weapon
```

#### Console Commands

**Runtime Debug Control:**

```cpp
// Enable/disable at runtime in Blueprint or C++
ULayeredTooltipSettings* Settings = ULayeredTooltipSettings::Get();
Settings->bLayeredTooltipDebug = true;
```

**Stat Display:**

1. Enter `Stat LayeredTooltip` in console window 
   
   ![5.Debug Features-20250802153329922.webp](/assets/Debug%20Features/5.Debug%20Features-20250802153329922.webp)
   
2. Check performance metrics 
   
   ![5.Debug Features-20250802153434841.webp](/assets/Debug%20Features/5.Debug%20Features-20250802153434841.webp)

#### Troubleshooting

**Common Debugging Scenarios:**

1. **When tooltips are not displayed**
    - Check trigger areas in debug mode
    - Verify registration status in logs
2. **When metadata is not properly transmitted**
    - Check raw metadata with debug text
    - Verify key names for typos or omissions
3. **Performance issue analysis**
    - Check number of registered triggers
    - Analyze frequent registration/unregistration patterns

#### Important Notes

- Debug mode may impact performance; use only during development
- Disable debug mode in packaged builds
- Some settings may require an engine restart