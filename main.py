import scene


if __name__ == '__main__':
    scene_manager = scene.SceneManager()
    first_scene = scene.Menu(scene_manager)
    scene_manager.next_scene = first_scene
    scene_manager.run()
