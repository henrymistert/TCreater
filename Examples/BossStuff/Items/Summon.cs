using Microsoft.Xna.Framework;
using Terraria;
using Terraria.ID;
using Terraria.ModLoader;
using static Terraria.ModLoader.ModContent;
using FunnyMod.Items;
using FunnyMod.NPCs;

namespace FunnyMod.Items
{
	// Making an item like Life Fruit (That goes above 500) involves a lot of code, as there are many things to consider. (An alternate that approaches 500 can simply follow vanilla code, however.):
	//    You can't make player.statLifeMax more than 500 (it won't save), so you'll have to maintain your extra life within your mod.
	//    Within your ModPlayer, you need to save/load a count of usages. You also need to sync the data to other players. 
	internal class Rumbling : ModItem
	{
		// public override string Texture => "Terraria/Item_" + ItemID.LifeFruit;

		public override void SetStaticDefaults() {
			Tooltip.SetDefault("Summons the colossal titan");
			DisplayName.SetDefault("Boss Summon");
		}

		public override void SetDefaults() {
			//item.color = Color.Purple;
			item.width = 26;
			item.height = 26;
			item.maxStack = 20;
			item.rare = ItemRarityID.LightRed;
			item.useAnimation = 45;
			item.useStyle = ItemUseStyleID.HoldingOut;
			item.consumable = true;
		}

		public override bool CanUseItem(Player player) {
			// Any mod that changes statLifeMax to be greater than 500 is broken and needs to fix their code.
			// This check also prevents this item from being used before vanilla health upgrades are maxed out.
			return !NPC.AnyNPCs(mod.NPCType("CollosalTitan"));
		}

		public override bool UseItem(Player player) {
			if(Main.dayTime == false)
            {
				NPC.SpawnOnPlayer(player.whoAmI, mod.NPCType("CollosalTitan"));
				return true;
            }
            else
            {
				return false;
            }
		}

		public override void AddRecipes() {
			ModRecipe recipe = new ModRecipe(mod);
			recipe.AddIngredient(ItemID.LifeCrystal, 10);
			recipe.SetResult(this, 1);
			recipe.AddRecipe();
		}
	}
}
