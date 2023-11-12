// src/main.rs

use amethyst::start_logger;

mod states;

fn main() -> amethyst::Result<()> {
    start_logger(Default::default());

    let app_root = application_root_dir()?;
    let display_config_path = app_root.join("config/display.ron");

    let game_data = GameDataBuilder::default()
        .with_bundle(
            RenderingBundle::<DefaultBackend>::new()
                .with_plugin(
                    RenderFlat2D::default()
                        .with_sprite_sheet_processor(),
                ),
        )?
        .build()?;

    let mut game = Application::new(
        app_root,
        states::DungeonCrawler,
        game_data,
    )?;

    game.run();
    Ok(())
}
