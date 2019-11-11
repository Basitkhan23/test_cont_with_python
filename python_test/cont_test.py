import conu

PORT = 5000

with conu.DockerBackend() as backend:
	image = backend.ImageClass( "nginx")
	options = ["-p", "8000:8000"]
	container = image.run_via_binary()

	try:
		assert container.is_running()
		container.wait_for_port(PORT)
	finally:
		container.stop()
		container.delete()
