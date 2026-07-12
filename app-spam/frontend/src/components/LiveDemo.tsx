import SpamForm from "./SpamForm";

type Props = {
    slug: string;
};

function LiveDemo({ slug }: Props) {

    switch (slug) {

        case "spam-email-detection":

            return (
                <section className="my-5">

                    <h2 className="mb-4">

                        Live Demo

                    </h2>

                    <SpamForm />

                </section>
            );

        default:

            return (
                <section className="my-5">

                    <h2 className="mb-4">

                        Live Demo

                    </h2>

                    <div className="alert alert-secondary">

                        This project is currently presented as a case study.
                        A live interactive demo will be available in a future release.

                    </div>

                </section>
            );
    }

}

export default LiveDemo;