// src/states/dungeon_crawler.rs

use amethyst::{
    core::transform::Transform,
    ecs::{Builder, World, WorldExt},
    input::{is_close_requested, is_key_down, VirtualKeyCode},
    prelude::*,
    renderer::{Camera, Material, MaterialDefaults, Mesh, MeshHandle, PosTex, Shape, Transparent},
    ui::{FontAsset, UiCreator, UiFinder, UiText, UiTransform},
    utils::application_root_dir,
};

pub struct DungeonCrawler;

impl SimpleState for DungeonCrawler {
    fn on_start(&mut self, data: StateData<'_, GameData<'_, '_>>) {
        let world = data.world;

        // Create the player entity
        create_player(world);

        // Generate walls
        generate_walls(world);
    }

    fn handle_event(&mut self, _: StateData<'_, GameData<'_, '_>>, event: StateEvent) -> SimpleTrans {
        if let StateEvent::Window(event) = &event {
            if is_close_requested(&event) || is_key_down(&event, VirtualKeyCode::Escape) {
                Trans::Quit
            } else {
                Trans::None
            }
        } else {
            Trans::None
        }
    }
}

fn create_player(world: &mut World) {
    let mut transform = Transform::default();
    transform.set_translation_xyz(400.0, 300.0, 0.0);

    world
        .create_entity()
        .with(transform)
        .with(UiTransform::new(
            "player".to_string(),
            0.0,
            0.0,
            1.0,
            1.0,
            0.0,
            0.0,
            0,
        ))
        .with(UiText::new(
            world.read_resource::<FontAsset>().0.clone(),
            "@".to_string(),
            [1.0, 1.0, 1.0, 1.0],
            20.0,
        ))
        .build();
}

fn generate_walls(world: &mut World) {
    for x in 0..10 {
        for y in 0..10 {
            let mut transform = Transform::default();
            transform.set_translation_xyz(x as f32 * 32.0, y as f32 * 32.0, 0.0);

            world
                .create_entity()
                .with(transform)
                .with(UiTransform::new(
                    format!("wall_{}_{}", x, y),
                    x as f32 * 32.0,
                    y as f32 * 32.0,
                    1.0,
                    1.0,
                    0.0,
                    0.0,
                    0,
                ))
                .with(UiText::new(
                    world.read_resource::<FontAsset>().0.clone(),
                    "#".to_string(),
                    [1.0, 1.0, 1.0, 1.0],
                    20.0,
                ))
                .build();
        }
    }
}
