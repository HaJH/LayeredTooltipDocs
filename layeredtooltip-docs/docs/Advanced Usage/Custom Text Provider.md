> Create custom text generation logic or integrate with any data source by implementing the `ILayeredTooltipTextProvider` interface.

##### Interface Implementation

**Blueprint Implementation:**

1. Add the `LayeredTooltipTextProvider` interface in the Blueprint's `Class Settings`. 
   
   ![Custom Text Provider-20250802151312529.webp](/assets/Custom%20Text%20Provider/Custom%20Text%20Provider-20250802151312529.webp)
   
2. Implement interface functions in Blueprint 
   
   ![Custom Text Provider-20250802151428204.webp](/assets/Custom%20Text%20Provider/Custom%20Text%20Provider-20250802151428204.webp) 
   
   ![Custom Text Provider-20250802151510647.webp](/assets/Custom%20Text%20Provider/Custom%20Text%20Provider-20250802151510647.webp) 
   
   ![Custom Text Provider-20250802151456795.webp](/assets/Custom%20Text%20Provider/Custom%20Text%20Provider-20250802151456795.webp)
   

**C++ Implementation:**

```cpp
UCLASS(BlueprintType, Blueprintable)
class UMyCustomTextProvider : public UObject, public ILayeredTooltipTextProvider
{
    GENERATED_BODY()
public:
    virtual void InitializeTextProvider_Implementation() override;
    virtual FText ResolveText_Implementation(const FLayeredToolTipTriggerData& TriggerData) override;
};
```

##### Registration in Plugin Settings

Configure the custom text provider class in `Project Settings → Plugins → LayeredTooltip Settings → Tooltip Text Provider Class`. 

![Custom Text Provider-20250802151656838.webp](/assets/Custom%20Text%20Provider/Custom%20Text%20Provider-20250802151656838.webp)

##### Advanced Text Processing Examples

**External Data Source Integration:**

```cpp
void UDatabaseTextProvider::InitializeTextProvider_Implementation()
{
    // Initialize database connection
    DatabaseConnection = CreateDatabaseConnection();
    
    // Integrate localization system
    LocalizationManager = GetGameInstance()->GetSubsystem<ULocalizationSubsystem>();
    
    // Build cache system
    TextCache.Reserve(1000);
}

FText UDatabaseTextProvider::ResolveText_Implementation(const FLayeredToolTipTriggerData& TriggerData)
{
    FString TextId = TriggerData.TooltipData.FindRef("TextId");
    FString Category = TriggerData.TooltipData.FindRef("Category");
    
    // Check cache
    FString CacheKey = FString::Printf(TEXT("%s_%s"), *Category, *TextId);
    if (FText* CachedText = TextCache.Find(CacheKey))
    {
        return *CachedText;
    }
    
    // Query database
    FText ResolvedText = QueryFromDatabase(Category, TextId);
    
    // Process dynamic variables
    ResolvedText = ProcessDynamicVariables(ResolvedText, TriggerData);
    
    // Cache result
    TextCache.Add(CacheKey, ResolvedText);
    
    return ResolvedText;
}
```

**Payload-Based Dynamic Text Generation:**

```cpp
FText UAdvancedTextProvider::ResolveText_Implementation(const FLayeredToolTipTriggerData& TriggerData)
{
    // Handle by payload type
    if (UItemData* Item = Cast<UItemData>(TriggerData.TriggerPayload))
    {
        return GenerateItemTooltip(Item, TriggerData.TooltipData);
    }
    else if (APlayerCharacter* Player = Cast<APlayerCharacter>(TriggerData.TriggerPayload))
    {
        return GeneratePlayerTooltip(Player, TriggerData.TooltipData);
    }
    
    return TriggerData.TooltipText;
}

FText UAdvancedTextProvider::GenerateItemTooltip(UItemData* Item, const TMap<FString, FString>& Metadata)
{
    FString TooltipText;
    
    // Basic information
    TooltipText += FString::Printf(TEXT("<title>%s</>\n"), *Item->GetDisplayName());
    
    // Dynamic stat calculation
    if (APlayerCharacter* Player = GetCurrentPlayer())
    {
        int32 EffectiveDamage = Item->CalculateDamageForPlayer(Player);
        TooltipText += FString::Printf(TEXT("Damage: %d\n"), EffectiveDamage);
    }
    
    // Generate nested tooltip links
    for (const FString& Material : Item->GetMaterials())
    {
        TooltipText += FString::Printf(TEXT("- <tooltip TextId=\"%s\">%s</>\n"), 
            *Material, *GetMaterialDisplayName(Material));
    }
    
    return FText::FromString(TooltipText);
}
```

##### Important Notes

- `ResolveText` is called every time a tooltip displays, so optimize for performance
- Handle heavy operations in `InitializeTextProvider` or implement caching